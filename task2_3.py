import json


def task():
    filename = "input.json"
    with open(filename) as f:
        dict_ = json.load(f)# TODO считать содержимое JSON файла
    dict_max = max(dict_, key= lambda x: x['score'])
    return dict_max  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
