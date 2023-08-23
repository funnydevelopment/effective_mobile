import json
import config


file_name = "data.json"
data = config.load_data(file_name)


def get_all_data():
    for row in data:
        print(json.dumps(row, indent=4))


def save_data():
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
        print("Новый пользователь добавлен в справочник.")
    except Exception:
        print(f"Произошла ошибка при добавлении пользователя")
