from text_messages import text_messages as texts


def user_greet():
    print(texts.HELLO_TEXT)


def user_choice() -> str:
    print(texts.CHOICE_TEXT)
    return input("\nВыберите действие: ")


def user_goodbye():
    print(texts.GOODBYE_TEXT)
