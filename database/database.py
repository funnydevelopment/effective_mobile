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
    try:
        new_person = {}
        last_name = input("Введите фамилию: ")
        new_person["last_name"] = last_name
        first_name = input("Введите имя: ")
        new_person["first_name"] = first_name
        middle_name = input("Введите отчество: ")
        new_person["middle_name"] = middle_name
        organization_name = input("Введите название организации: ")
        new_person["organization_name"] = organization_name
        work_phone = input("Введите телефон рабочий: ")
        new_person["work_phone"] = work_phone
        personal_phone = input("Введите телефон личный (сотовый): ")
        new_person["personal_phone"] = personal_phone
        data.append(new_person)
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(texts.SAVE_DATA_TEXT_2)
    except Exception:
        print(texts.SAVE_DATA_TEXT_3)


def get_persons_count() -> None:
    print(f"\nОбщее количество записей в справочнике: {len(data)}\n")
