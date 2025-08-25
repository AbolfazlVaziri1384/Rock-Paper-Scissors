import random

ITEMS = {1: "Rock", 2: "Paper", 3: "Scissors"}

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def choose_system():
    return random.randint(1, 3)


def get_status(system, client):
    base_msg = f"You chose {ITEMS[client]}. System chose {ITEMS[system]}.\n"
    if system == client:
        return YELLOW + base_msg + "It's a tie!" + RESET
    elif (
        (system == 1 and client == 3)
        or (system == 2 and client == 1)
        or (system == 3 and client == 2)
    ):
        return RED + base_msg + "System wins!" + RESET
    else:
        return GREEN + base_msg + "You win!" + RESET


def main():
    """
    Runs the main loop for the Rock-Paper-Scissors game.

    Continuously prompts the user to select Rock, Paper, or Scissors, or to exit the game.
    Handles invalid input and displays appropriate messages.
    After a valid selection, generates the system's choice and displays the result.
    Exits gracefully when the user chooses to exit.

    User Input:
        - 1: Rock
        - 2: Paper
        - 3: Scissors
        - -1: Exit

    Returns:
        None
    """
    while True:
        while True:
            try:
                client = int(
                    input(
                        BLUE
                        + "1: Rock, 2: Paper, 3: Scissors\nPlease choose one (1-3, or -1 to exit): "
                        + RESET
                    )
                )
                if client == -1:
                    print(BLUE + "Thanks for playing! See you later!" + RESET)
                    return
                if client in ITEMS:
                    break
                print(
                    RED
                    + "Invalid choice. Please select 1, 2, 3, or -1 to exit."
                    + RESET
                )
            except ValueError:
                print(
                    RED
                    + "Invalid input. Please enter a number (1-3, or -1 to exit)."
                    + RESET
                )
        system = choose_system()
        print(get_status(system, client))


if __name__ == "__main__":
    main()