from text_messages import text_messages as texts


def user_greet() -> None:
    print(texts.HELLO_TEXT)


def user_choice() -> str:
    print(texts.CHOICE_TEXT)
    return input("\nВыберите действие: ")


def user_goodbye() -> None:
    print(texts.GOODBYE_TEXT)
