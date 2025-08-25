import random

ITEMS = {1: "Rock", 2: "Paper", 3: "Scissors"}


def choose_system():
    return random.randint(1, 3)


def get_status(system, client):
    if system == client:
        return f"You chose {ITEMS[client]}. System chose {ITEMS[system]}.\nIt's a tie!"
    elif (
        (system == 1 and client == 3)
        or (system == 2 and client == 1)
        or (system == 3 and client == 2)
    ):
        return (
            f"You chose {ITEMS[client]}. System chose {ITEMS[system]}.\n"
            "System wins!"
        )
    else:
        return (
            f"You chose {ITEMS[client]}. System chose {ITEMS[system]}.\n"
            "You win!"
        )


def main():
    while True:
        while True:
            try:
                client = int(
                    input("1: Rock, 2: Paper, 3: Scissors\nPlease choose one (1-3, or -1 to exit): ")
                )
                if client == -1:
                    print("Thanks for playing! See you later!")
                    return
                if client in ITEMS:
                    break
                print("Invalid choice. Please select 1, 2, 3, or -1 to exit.")
            except ValueError:
                print("Invalid input. Please enter a number (1-3, or -1 to exit).")
        system = choose_system()
        print(get_status(system, client))


if __name__ == "__main__":
    main()