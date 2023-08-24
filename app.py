from database import database
from views import views
from text_messages import text_messages as texts


def main():
    views.user_greet()
    while True:
        choice = views.user_choice()

        match choice:
            case "1":
                database.get_all_data()
            case "2":
                database.save_data()
            case "3":
                views.update_user_data()
            case "4":
                key_to_search = input("Введите ключ для поиска: ")
                value_to_search = views.user_full_name()
                database.search_data(key_to_search, value_to_search)
            case "5":
                database.get_persons_count()
            case "6":
                return views.user_goodbye()
            case _:
                print(texts.WRONG_INPUT_TEXT)


if __name__ == "__main__":
    main()
