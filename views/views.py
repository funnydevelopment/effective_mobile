from text_messages import text_messages as texts
from database import database


def user_greet() -> None:
    print(texts.HELLO_TEXT)


def user_choice() -> str:
    print(texts.CHOICE_TEXT)
    return input("\nВыберите действие: ")


def user_input_alpha(input_word: str) -> str | bool:
    if input_word.isalpha():
        return input_word
    return False


def user_input_digit(input_word: str) -> str | bool:
    if input_word.isdigit():
        return input_word
    return False


def user_full_name() -> str:
    part_of_name = input()
    if part_of_name.isalpha():
        return part_of_name
    else:
        raise TypeError


def user_goodbye() -> bool:
    print(texts.GOODBYE_TEXT)
    return False


def update_user_data():
    def get_valid_input(prompt, validation_func):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            else:
                print("Некорректный ввод. Попробуйте ещё раз.")

    last_name_check = get_valid_input(
        "Введите фамилию для обновления: ", user_input_alpha
    )
    last_name_exists = database.if_user_exist(last_name_check)

    if last_name_exists:
        last_name = get_valid_input("Введите новую фамилию: ", user_input_alpha)
        first_name = get_valid_input("Введите новое имя: ", user_input_alpha)
        middle_name = get_valid_input("Введите новое отчество: ", user_input_alpha)
        organization_name = input("Введите новое название организации: ")
        work_phone = get_valid_input("Введите рабочий телефон: ", user_input_digit)
        personal_phone = get_valid_input("Введите личный телефон: ", user_input_digit)
        updated_fields = {
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "organization_name": organization_name,
            "work_phone": work_phone,
            "personal_phone": personal_phone,
        }
        database.update_data(last_name_check, updated_fields)
    else:
        print(texts.NO_USER_TEXT)
