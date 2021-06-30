import csv
import json
import os
from pathlib import Path

import jsonpath as jsonpath

BASE_PATH = Path.cwd().joinpath("asset")
test_data = []


def read_data_from_json_file(file_name):
    path = get_path(file_name)
    with path.open(mode="r") as schema_file:
        return json.load(schema_file)


def read_data_from_csv_file(file_name):

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


def read_data(file):
    """Чтение csv файла в list of jsons"""
    with open(f'{file}', "r", encoding='utf-8') as f:
        dict_reader = csv.DictReader(f, delimiter=";")
        for row in dict_reader:
            dict_from_csv = dict(row)
            test_data.append(dict_from_csv)

    return test_data


def write_scv_to_list_dict_file(file, name):
    """ Чтение данных из csv в корне проекта и запись в файл как list of jsons """
    dicts = read_data(file)
    file_name = os.getcwd() + f"/assets/assets_{name}.py"
    with open(file_name, "a+", encoding="utf-8") as f:
        json.dump(dicts, f, ensure_ascii=False, sort_keys=True, indent=4)


def search_data_from_json_to_list_of_jsons(base_file: json, jsonpath_expression: str):
    """метод для получения list required полей из openApi
    в зависимости от endpoint запроса и статуса response"""
    list_jsons = jsonpath.jsonpath(base_file, jsonpath_expression)
    return list_jsons


def write_json_file(base_name, json_object: json):
    """Too do """
    file_name = os.getcwd() + f"/assets/{base_name}.json"
    with open(file_name, "a+", encoding="utf-8") as f:
        json.dump(json_object, f, ensure_ascii=False, sort_keys=True, indent=4)