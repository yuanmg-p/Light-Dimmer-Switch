def adjust_light(level):
    if level == 0:
        print("Turning off the light.")
    elif level == 1:
        print("Setting light to Low (25%).")
    elif level == 2:
        print("Setting light to Medium (50%).")
    elif level == 3:
        print("Setting light to High (75%).")
    elif level == 4:
        print("Setting light to Maximum (100%).")
    else:
        print("Invalid input! Please enter a number between 0 and 4.")


def main():
    while True:
        print("\nLight Dimmer Switch:")
        print("Press 0 = Off, Press 1 = Low, Press 2 = Medium, Press 3 = High, Press 4 = Maximum")
        choice = input("Enter your choice (0-4): ")
        try:
            choice = int(choice)
            if 0 <= choice <= 4:
                adjust_light(choice)
                if choice == 0:
                    break
            else:
                print("Invalid input! Please enter a number between 0 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
