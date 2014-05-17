import json

def get_current_gas_station_map():
    with open('../datasets/gas_stations_data.json', 'r') as json_txt:
        json_dict = json.load(json_txt)
        gas_stations = json_dict.get('gas_stations')

        gas_station_map = {}
        for gas_station in gas_stations:
            gas_station_map[gas_station.get('id')] = gas_station

        return gas_station_map

def extract_lat_lon_from_map(gas_station_map):
    extract = lambda key: (
            gas_station_map[key].get('latitude'), 
            gas_station_map[key].get('longitude'),
            key
        )
    return sorted(map(extract, gas_station_map))

