from datetime import date

from utils import add, divide, multiply, subtract


def main():
    print("Name: Fahim Faisal Deepto")
    print(f"Today's date: {date.today().isoformat()}")

    # Demo basic calculator functions
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(5, 3) = {subtract(5, 3)}")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
    print(f"divide(6, 3) = {divide(6, 3)}")

    # Demo error handling
    try:
        print(f"divide(5, 0) = {divide(5, 0)}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    try:
        print(f"add(5, 'a') = {add(5, 'a')}")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
