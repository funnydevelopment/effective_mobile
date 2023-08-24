from typing import Callable

from text_messages import text_messages as texts
from database import database


def user_greet() -> None:
    """
    Приветственное сообщение пользователю
    :return:
    """
    print(texts.HELLO_TEXT)


def user_choice() -> str:
    """
    Ожидание выбора пользователя для вызова необходимой функции
    :return:
    """
    print(texts.CHOICE_TEXT)
    return input("\nВыберите действие: ")


def get_valid_input(prompt: str, validation_func: Callable[[str], bool]) -> str:
    """
    Функция для проверки данных при вводе данных
    :param prompt: строка для функции input
    :param validation_func: вызов функции для проверки
    :return: возвращаем валидные данные
    """
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(texts.WRONG_INPUT_TEXT_2)


def user_input_alpha(input_word: str) -> str | bool:
    """
    Переданная строка состоит ли из букв, используем для ФИО
    :param input_word:
    :return: False помогает печатать необходимое сообщение и повторить ввод текста
    """
    if input_word.isalpha() and len(input_word) > 3:
        return input_word
    return False


def user_input_digit(input_word: str) -> str | bool:
    """
    Переданная строка состоит ли из цифр, используем для номеров
    :param input_word:
    :return: False помогает печатать необходимое сообщение и повторить ввод текста
    """
    if input_word.isdigit() and len(input_word) == 11:
        return input_word
    return False


def goodbye_user() -> bool:
    """
    Прощальное сообщение пользователю
    :return: False, чтобы остановить цикл while
    """
    print(texts.GOODBYE_TEXT)
    return False


def save_user() -> None:
    """
    Проверяем корректность данных и вызываем функцию сохранения данных
    :return:
    """
    print(texts.SAVE_DATA_TEXT_1)
    print(texts.JSON_DATA_TEXT)
    new_person = dict()
    new_person["last_name"] = get_valid_input(
        "Введите фамилию нового пользователя: ", user_input_alpha
    )
    new_person["first_name"] = get_valid_input(
        "Введите имя нового пользователя: ", user_input_alpha
    )
    new_person["middle_name"] = get_valid_input(
        "Введите отчество нового пользователя: ", user_input_alpha
    )
    new_person["organization_name"] = input("Введите новое название организации: ")
    new_person["work_phone"] = get_valid_input(
        "Введите рабочий телефон: ", user_input_digit
    )
    new_person["personal_phone"] = get_valid_input(
        "Введите личный телефон: ", user_input_digit
    )
    database.save_data(new_person)


def update_user() -> None:
    """
    Проверяем корректность данных и вызываем функцию обновления данных
    :return:
    """
    last_name_check = get_valid_input(
        "\nВведите фамилию для обновления: ", user_input_alpha
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


def search_user() -> None:
    """
    Преобразовываем в список входящую строку и вызываем функцию поиска
    :return:
    """
    print(texts.JSON_DATA_TEXT)
    list_to_search = input(texts.SEARCH_INPUT_TEXT).split()
    database.search_data(list_to_search)
