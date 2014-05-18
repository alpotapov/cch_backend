import json


def arrive_to_gas_station():
    fo = open('datasets/fixtures/arrive_to_gas_station.json', 'r')
    entries = json.load(fo)

    fo = open('datasets/fake_cci.json', 'r+')
    fo.seek(0)
    json.dump(entries, fo)
    fo.truncate()
    fo.close()