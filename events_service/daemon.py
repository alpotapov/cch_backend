import json
import time

processed_entries = []

while True:
    with open('bla.json', 'r') as txt:
        test = json.load(txt)
        for entry in test:
            if entry['id'] in processed_entries:
                continue
            print entry['name']
            processed_entries.append(entry['id'])

    print('+++++++')
    time.sleep(5)