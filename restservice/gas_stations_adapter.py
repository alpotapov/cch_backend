import json

def get_current_gas_station_map():
    with open('../datasets/gas_stations_data.json', 'r') as json_txt:
        json_dict = json.load(json_txt)
        gas_stations = json_dict.get('gas_stations')

        gas_station_map = {}
        for gas_station in gas_stations:
            gas_station_map[gas_station.get('id')] = gas_station

        return gas_station_map
