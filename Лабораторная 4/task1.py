# TODO решите задачу
import json

FILE_NAME = 'input.json'


def task() -> float:
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)
        file.close()
    return round(sum([item["score"] * item["weight"] for item in data]), 3)


print(task())
