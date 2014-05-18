from local_connected_car_adapter import get_vehicle_data_by_ccid
import os, time, json
from restservice.service_abstraction import get_all_stations_near_ccid
from models import CCIEntry

class Events ():
    def event_engine_stop(self, entry):
        stations = get_all_stations_near_ccid(
            lat=entry['latitude'],
            lon=entry['longitude'],
            angle=entry['GPS_DIR'],
            km_threshold=0.1
        )
        print 'checking...'
        if 0 < len(stations) < 3:
            print 'push sent'
            pass

def check_modification_time():
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file_path)
    return mtime


def save_processed(entry):
    entry = CCIEntry(
        recorded_at=entry['recorded_at'],
        longitude=entry['longitude'],
        latitude=entry['latitude'],
        MDI_OBD_MILEAGE=entry['MDI_OBD_MILEAGE']['1'],
        MDI_OBD_FUEL=entry['MDI_OBD_FUEL']['1'],
        GPS_DIR=entry['GPS_DIR'],
        GPS_SPEED=entry['GPS_SPEED']['1'],
        IGNITION=entry['IGNITION']
    )

    entry.save()


def parse_and_clean_file():
    fo = open(file_path, 'r+')
    try:
        entries = json.load(fo)
    except ValueError:
        return []

    for entry in entries:
        save_processed(entry)

    fo.seek(0)
    fo.write('')
    fo.truncate()
    fo.close()

    return entries


def run():
    last_recorded_file_modification = check_modification_time()
    while True:
        if check_modification_time() > last_recorded_file_modification:
            entries = parse_and_clean_file()
            for i in xrange(len(entries)):
                if entries[i]['IGNITION'] == False:
                    print 'event triggered'
                    Events().event_engine_stop(entries[i])

        last_recorded_file_modification = check_modification_time()

        print '++++++'
        time.sleep(5)

file_path = 'datasets/fake_cci.json'
processed_file_path = 'datasets/processed_car_engine_start_stop.json'
