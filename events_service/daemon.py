import json
import time
from restservice import gas_stations_adapter

class EventHandler():
    def __init__(self):
        pass

    def event_engine_stop(self, entry):
        # merge with master and check if stopped at gas station
        result = True
        if result:
            print 'Sending push to user'
            # send push notification to user
            pass

    def process(self, entry):
        # pattern 1: stop at gas station
        if entry['DIO_IGNITION'] == False:
            self.event_engine_stop(entry)


def close_file(obj):
    open("engine_stops.json", "w").write(
        json.dumps(obj, sort_keys=False, indent=4, separators=(',', ': '))
    )


event_handler = EventHandler()

while True:
    obj = json.load(open('engine_stops.json', 'r'))
    for i in xrange(len(obj)):
        event_handler.process(obj[i])
        obj.pop(i)

    close_file(obj)
    print('+++++++')
    time.sleep(5)