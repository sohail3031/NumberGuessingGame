from random import randrange


class NumberGuess:
    def __init__(self) -> None:
        self.__start_number: int = int()
        self.__end_number: int = int()
        self.__random_number: int = int()
        self.__number_of_attempts: int = 0
        self.__guess_limit: int = 15
        self.__win: int = 0
        self.__lose: int = 0
        self.__current_win_streak: int = 0
        self.__maximum_win_streak: int = 0
        self.__current_lose_streak: int = 0
        self.__maximum_lose_streak: int = 0

    # Method to Read the Start Number
    def __get_start_number(self) -> None:
        while True:
            try:
                self.__start_number = int(input("Enter the Start Value: "))

                break
            except ValueError:
                print("Please Enter a Valid Number!")

    # Method to Read the End Number
    def __get_end_number(self) -> None:
        while True:
            try:
                self.__end_number = int(input("Enter the End Number: "))

                break
            except ValueError:
                print("Please Enter a Valid Number!")

    # Method to Generate the Random Number
    def __generate_random_number(self) -> None:
        self.__random_number = randrange(self.__start_number, self.__end_number + 1)

    def __check_win_condition(self, guess: int) -> bool:
        self.__number_of_attempts += 1
        self.__guess_limit -= 1

        if guess.__eq__(self.__random_number):
            self.__win += 1

            print("Congratulations You Won! 🥳🥳🥳🥳🥳🥳🥳🥳🥳")

            return True
        elif guess in range((self.__random_number - 10), (self.__random_number + 10)):
            print("Hot 🔥")
        else:
            print("Cold ❄️")

        return False

    # Game Loop Method
    def __game_loop(self) -> None:
        while True:
            try:
                if self.__guess_limit <= 0:
                    self.__lose += 1
                    print(f"\nOops! The Current Number was {self.__random_number}! Guess Limit is Over! Try Again!")

                    break

                __user_guess = int(input("\nGuess the Number: "))

                if self.__check_win_condition(__user_guess):
                    break
            except ValueError:
                print("Please Enter a Valid Number!")

    def __reset_game_data(self) -> None:
        self.__number_of_attempts = 0
        self.__guess_limit = 15

    # Main method
    def main(self) -> None:
        while True:
            self.__reset_game_data()
            self.__get_start_number()
            self.__get_end_number()
            self.__generate_random_number()
            self.__game_loop()

            print(f"\nYou took {self.__number_of_attempts} attempts!\n")
            print(f"Wins: {self.__win}, Lose: {self.__lose}")

            if not input("\nDo You Want to Play Again? [Y | N]: ").lower().__eq__("y"):
                break

            print()


if __name__ == "__main__":
    NumberGuess().main()
