import json
import os


def load_data(file_name: str) -> json:
    """
    Находим нужен файл json формата и возвращаем содержимое
    :param file_name:
    :return:
    """
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    else:
        return {}
