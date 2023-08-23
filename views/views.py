from text_messages import text_messages as texts


def user_greet() -> str:
    print(texts.HELLO_TEXT)
    return input("Выберите действие: ")
