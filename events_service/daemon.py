import json
import time

processed_entries = []

class EventHandler():
    def __init__(self):
        pass

    def process(self, entry):
        # pattern 1: stop at gas station
        if not entry['DIO_IGNITION']:
            

while True:
    with open('engine_stops.json', 'r') as txt:
        entries = json.load(txt)
        for entry in entries:
             entry['name']
            processed_entries.append(entry['id'])

    print('+++++++')
    time.sleep(5)