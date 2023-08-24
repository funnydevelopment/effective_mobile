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
                views.save_user()
            case "3":
                views.update_user()
            case "4":
                views.search_user()
            case "5":
                database.get_persons_count()
            case "6":
                return views.goodbye_user()
            case _:
                print(texts.WRONG_INPUT_TEXT)


if __name__ == "__main__":
    main()
