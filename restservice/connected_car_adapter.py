import json

def get_vehicle_data_by_ccid(ccid):
    # just returning somewhat valid data
    with open('datasets/car_mock.json', 'r') as json_txt:
        mock = json.load(json_txt)[0]
        mock['MDI_OBD_FUEL'] = mock.get('MDI_OBD_FUEL')['1']
        mock['MDI_OBD_MILEAGE'] = mock.get('MDI_OBD_MILEAGE')['1']
        mock['GPS_SPEED'] = mock.get('GPS_SPEED')['1']

    return mock
