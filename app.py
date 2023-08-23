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
                pass
            case "4":
                pass
            case "5":
                database.get_persons_count()
            case "6":
                views.user_goodbye()
                break
            case _:
                print(texts.WRONG_INPUT_TEXT)


if __name__ == "__main__":
    main()
