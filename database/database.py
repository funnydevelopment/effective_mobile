import json

from config import config
from text_messages import text_messages as texts


file_name = "database/data.json"
data = config.load_data(file_name)


def get_all_data() -> None:
    print(texts.GET_ALL_DATA_TEXT)
    for row in data:
        print(json.dumps(row, indent=4))


def save_data() -> None:
    print(texts.SAVE_DATA_TEXT_1)
    print(texts.JSON_DATA_TEXT)
    try:
        new_person = {}
        fields = [
            "last_name",
            "first_name",
            "middle_name",
            "organization_name",
            "work_phone",
            "personal_phone",
        ]
        for field in fields:
            value = input(f"Введите {field.replace('_', ' ')}: ")
            new_person[field] = value
        data.append(new_person)
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


def search_data(key: str, value: str):
    print(texts.JSON_DATA_TEXT)
    for entry in data:
        if entry[key] == value:
            print(entry)


def get_persons_count() -> None:
    print(f"\nОбщее количество записей в справочнике: {len(data)}\n")
