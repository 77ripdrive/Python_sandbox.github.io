import csv
import json
from pathlib import Path

BASE_PATH = Path.cwd().joinpath("asset")


def read_data_from_json_file(file_name):
    path = get_path(file_name)
    with path.open(mode="r") as schema_file:
        return json.load(schema_file)


def read_data_from_csv_file(file_name):
    test_data = []
    path = get_path(file_name)
    with path.open(mode="r") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)
        for row in data:
            test_data.append(row)
    return test_data


def get_path(file_name):
    if ".json" in file_name:
        path = BASE_PATH.joinpath(file_name)
    elif ".csv" in file_name:
        path = BASE_PATH.joinpath(file_name)
    return path
