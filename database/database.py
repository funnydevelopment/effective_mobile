import json

from config import config
from text_messages import text_messages as texts


file_name = "database/data.json"
data = config.load_data(file_name)


def get_all_data() -> None:
    print(texts.GET_ALL_DATA_TEXT)
    for row in data:
        print(json.dumps(row, indent=4))


def save_data(user_data: dict) -> None:
    try:
        data.append(user_data)
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(texts.SAVE_DATA_TEXT_2)
    except Exception:
        print(texts.SAVE_DATA_TEXT_3)


def if_user_exist(last_name: str) -> bool:
    for entry in data:
        if entry["last_name"] == last_name:
            return True
    return False


def update_data(last_name_to_update: str, updated_fields: dict) -> None:
    for entry in data:
        if entry["last_name"] == last_name_to_update:
            entry.update(updated_fields)
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            print(texts.UPDATED_SUCCESSFULLY_TEXT)
            return


def search_data(search_data: str | list):
    if len(search_data) == 1:
        for entry in data:
            for key, value in entry.items():
                if search_data[0] in value.lower():
                    print(json.dumps(entry, indent=4))
                    return
            print(texts.NO_USER_TEXT)
            return
    else:
        print("Too many arguments")


def get_count_of_users() -> None:
    print(texts.TOTAL_USERS_TEXT.format(count=len(data)))
