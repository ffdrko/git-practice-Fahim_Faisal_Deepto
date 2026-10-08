from datetime import date

from utils import add, subtract


def main():
    print("Name: Fahim Faisal Deepto")
    print(f"Today's date: {date.today().isoformat()}")

    # Demo basic calculator functions
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(5, 3) = {subtract(5, 3)}")


if __name__ == "__main__":
    main()
