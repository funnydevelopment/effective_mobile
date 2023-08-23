import database
import views


def main():
    while True:
        choice = views.user_greet()

        if choice == "1":
            database.get_all_data()

        elif choice == "2":
            database.save_data()

        elif choice == "3":
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()
