import service_abstraction as apis
from models import Recommendation, User

KM_THRESHOLD = 15


def get_recommendations_for_ccid(ccid):
    response = {}
    
    current_user = apis.get_current_user_details(ccid)

    response['usercontext'] = {
        'longitude': current_user['longitude'],
        'latitude': current_user['latitude'],
        'gps_dir': current_user['GPS_DIR']
    }

    user = User.objects.get(connected_car_id=ccid)

    fuel_preference = user.fuel_type
        
    recommendations = []
    stations = apis.get_all_stations_near_ccid(ccid, KM_THRESHOLD)
    for station in stations:
        curr_dist = station[0][0]
        curr_angle_delta = station[0][1]
        curr_key = station[1]

        curr_details = apis.gas_map[curr_key]

        try:
            if fuel_preference == 0:
                curr_price = curr_details['prices']['price_diesel']
            elif fuel_preference == 1:
                curr_price = curr_details['prices']['price_superE10']
            else:
                curr_price = curr_details['prices']['price_superE5']
        except KeyError:
            continue

        if curr_price is None:
            continue

        rating = calculate_rating(curr_dist, curr_angle_delta)

        curr_recommendation = Recommendation(
            user=user,
            rating=rating,
            gas_station_id=curr_key,
            longitude=curr_details['longitude'],
            latitude=curr_details['latitude'],
            name=curr_details['name'],
            brand=curr_details['brandname'],
            address=curr_details['address'],
            zip_code=curr_details['zipcode'],
            city=curr_details['city'],
            price=curr_price 
        )
        curr_recommendation.save()

        recommendations.append(curr_recommendation)

    recommendations = sorted(recommendations, key=lambda recommendation: recommendation.rating)
    recommendations = recommendations[-10:]
    recommendations.reverse()
    response['recommendations'] = recommendations
    return response

def calculate_rating(distance, angle_delta):
    score = 0
    distance += 0.001 # avoid division by 0
    score += (1/distance)*5

    # reduce score for a bigger delta
    score *= pow((180-angle_delta)/angle_delta,2)

    return score
