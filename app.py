from database import database
from views import views


def main():
    while True:
        choice = views.user_greet()

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
                pass
            case "6":
                break
            case _:
                print("Неверный выбор.")


if __name__ == "__main__":
    main()
