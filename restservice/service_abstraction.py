from math import radians, cos, sin, asin, sqrt, atan2, degrees

import gas_stations_adapter as gas_api
import connected_car_adapter as car_api

gas_map = gas_api.get_current_gas_station_map()
gas_locations = gas_api.extract_lat_lon_from_map(gas_map)

def get_current_user_details(ccid):
    return car_api.get_vehicle_data_by_ccid(ccid)

def get_all_stations_near_ccid(km_threshold, ccid='', lat=0, lon='', angle=''):
    if ccid != '':
        vehicle_data = get_current_user_details(ccid)

        lat = vehicle_data['latitude']
        lon = vehicle_data['longitude']
        angle = vehicle_data['GPS_DIR']

    get_distance = lambda (gas_lat, gas_lon, gas_id): (
            haversine(lat, lon, gas_lat, gas_lon), 
            gas_id
        )
    filter_near = lambda ((km, angle), gas_id): km < km_threshold

    all_stations = map(get_distance, gas_locations)
    near_stations = filter(filter_near, all_stations)

    near_stations = sorted(near_stations, key=lambda tup:tup[0][0])

    compute_delta_angle = lambda ((gas_km, gas_angle), gas_id): (
            (
                gas_km, 
                min(((gas_angle-angle)+360)%360, ((angle-gas_angle)+360)%360)
            ),
            gas_id
        )

    return map(compute_delta_angle, near_stations)

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 

    bearing = atan2(cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(lon2-lon1), sin(lon2-lon1)*cos(lat2)) 
    bearing = (degrees(bearing) + 360)%360

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km, bearing
