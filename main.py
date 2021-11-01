import csv
import json

from constants import CSV_FILE, JSON_FILE, READ, WRITE, DATE, TYPE, AMOUNT


def woodalls_core():
    sample_data = open(CSV_FILE, READ)
    output_data = open(JSON_FILE, WRITE)
    fieldnames = (DATE, TYPE, AMOUNT)
    reader = csv.DictReader(sample_data, fieldnames)
    for row in reader:
        json.dump(row, output_data)
        output_data.write('\n')


if __name__ == "__main__":
    woodalls_core()
