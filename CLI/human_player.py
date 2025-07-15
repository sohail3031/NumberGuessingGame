import keyboard
import random
import math

from abc import ABC
from game_interface import GameInterface


class HumanPlayer(GameInterface, ABC):
    def __init__(self) -> None:
        super().__init__()

        self.__start_number: int = int()
        self.__end_number: int = int()
        self.__random_number: int = int()
        self.__number_of_attempts: int = 0
        self.__guess_limit: int = 15
        self.__total_wins: int = 0
        self.__total_lose: int = 0
        self.__current_win_streak: int = 0
        self.__maximum_win_streak: int = 0
        self.__hint_limit = 15
        self.__hint_types: list[str] = ["even-odd", "digit-length", "divisible", "multiple", "start-number",
                                        "end-number", "digits-sum", "ascending-descending", "between-x-y",
                                        "first-second-half", "prime", "square", "product"]

    def _get_start_number(self) -> None:
        while True:
            try:
                self.__start_number = int(input("\nEnter the Start Number: "))

                if self.__start_number < 0:
                    print("\nPlease Enter a Positive Number!\n")
                else:
                    break
            except ValueError:
                print("\nPlease Enter a Valid Input!\n")

    def _get_end_number(self) -> None:
        while True:
            try:
                self.__end_number = int(input("Enter the End Number: "))

                if self.__end_number <= self.__start_number:
                    print("\nThe End Number Should be Greater Than Start Number")
                else:
                    break
            except ValueError:
                print("\nPlease Enter a Valid Input!\n")

    def _generate_random_number(self) -> None:
        self.__random_number = random.randrange(self.__start_number, self.__end_number + 1)

        print(f"Random Number: {self.__random_number}")

    def _check_win_condition(self, user_guess: int) -> bool:
        if self.__random_number.__eq__(user_guess):
            self.__total_wins += 1
            self.__current_win_streak += 1
            self.__maximum_win_streak = self.__maximum_win_streak + 1 if self.__current_win_streak > self.__maximum_win_streak else self.__maximum_win_streak

            print("\nCongratulations You Won! 🥳🥳🥳🥳🥳🥳🥳🥳")
            print(f"You Took {self.__number_of_attempts} to Guess the Number!\n")

            return True
        elif user_guess in range((self.__random_number - 5), (self.__random_number + 6)):
            print("Hot 🔥🔥")
        elif user_guess in range((self.__random_number - 10), (self.__random_number + 11)):
            print("Warm 🔥")
        else:
            print("Cold ❄️")

        print(f"\nNumber of Guesses Left: {self.__guess_limit}\n")

        return False

    def _game_loop(self) -> None:
        while True:
            try:
                if not self.__guess_limit > 0:
                    self.__total_lose += 1
                    self.__current_win_streak = 0

                    print(f"Oops, You Ran Out of Guesses! The Correct Number Was {self.__random_number}. \nBetter Luck "
                          + "Next Time!\n")

                    break

                __user_guess: int = int(input("Guess the Number: "))
                self.__number_of_attempts += 1
                self.__guess_limit -= 1

                __result: bool = self._check_win_condition(user_guess=__user_guess)

                if __result:
                    break
            except ValueError:
                print("\nPlease Enter a Valid Number!\n")

    def __reset_game_data(self) -> None:
        self.__number_of_attempts = 0
        self.__guess_limit = 15
        self.__hint_limit = 15
        self.__hint_types = ["even-odd", "digit-length", "divisible", "multiple", "start-number", "end-number",
                             "digits-sum", "ascending-descending", "between-x-y", "first-second-half", "prime",
                             "square", "product"]

    def __hint_divisible_and_multiple(self, get_hint_type) -> None:
        for i in range(2, self.__random_number + 1):
            if i == self.__random_number:
                continue

            if self.__random_number % i == 0:
                print(f"\n💡 The Number is {get_hint_type.title()} of {i}")

                break
        else:
            print(f"\n💡 There is no {get_hint_type.title()} Available")

    def __hint_ascending_descending(self) -> None:
        __temp: list[int] = [int(i) for i in str(self.__random_number)]

        if all([__temp[i] <= __temp[i + 1] for i in range(len(__temp) - 1)]):
            print("\n💡 The Digits of the Number is in Ascending Order")
        elif all([__temp[i] >= __temp[i + 1] for i in range(len(__temp) - 1)]):
            print("\n💡 The Digits of the Number is in Descending Order")
        else:
            print("\n💡 The Digits of the Number is not in any Particular Order")

    def __hint_prime(self) -> None:
        if self.__random_number <= 1:
            print(f"\n💡 The Number is Non Prime")

        for i in range(2, int(math.sqrt(self.__random_number)) + 1):
            if self.__random_number % i == 0:
                print(f"\n💡 The Number is Non Prime")

                break
        else:
            print(f"\n💡 The Number is Prime")

    def __hint_square(self) -> None:
        for i in range(1, self.__random_number + 1):
            if i * i == self.__random_number:
                print(f"\n💡 The Number is a Square of {i}")

                break
        else:
            print(f"\n💡 The Number is not a Perfect Square")

    def __hint_product(self) -> None:
        products: list[int] = []

        for i in range(2, self.__random_number + 1):
            if i == self.__random_number:
                continue

            if self.__random_number % i == 0:
                products.append(i)

        if products:
            for i in range(len(products)):
                for j in range(i, len(products)):
                    if products[i] * products[j] == self.__random_number:
                        print(f"\n💡 The Products of the Number is {products[i]} and {products[j]}")

                        return
            else:
                print(f"\n💡 No Products of this Number Exists")
        else:
            print(f"\n💡 No Products of this Number Exists")

    def _show_hints(self) -> None:
        if self.__hint_limit > 0:
            self.__hint_limit -= 1
            __get_hint_type = random.choice(self.__hint_types)

            if __get_hint_type.__eq__("even-odd"):
                print(f"\n💡 The Number is {'Even' if self.__random_number % 2 == 0 else 'Odd'}")
            elif __get_hint_type.__eq__("digit-length"):
                print(f"\n💡 It's a {len(str(self.__random_number))} digit's number")
            elif __get_hint_type.__eq__("divisible") or __get_hint_type.__eq__("multiple"):
                self.__hint_divisible_and_multiple(get_hint_type=__get_hint_type)
            elif __get_hint_type.__eq__("start-number"):
                print(f"\n💡 The Number Starts with {str(self.__random_number)[0]}")
            elif __get_hint_type.__eq__("end-number"):
                print(f"\n💡 The Number Ends with {str(self.__random_number)[-1]}")
            elif __get_hint_type.__eq__("digits-sum"):
                print(f"\n💡 The Sum of the Digits is {sum([int(i) for i in str(self.__random_number)])}")
            elif __get_hint_type.__eq__("ascending-descending"):
                self.__hint_ascending_descending()
            elif __get_hint_type.__eq__("between-x-y"):
                print(f"\n💡 The Number is in Between {self.__random_number - 15} and {self.__random_number + 16}")
            elif __get_hint_type.__eq__("first-second-half"):
                print(f"\n💡 The Number Lies in "
                      f"{'First' if self.__random_number <= (self.__end_number / 2) else 'Second'} Half")
            elif __get_hint_type.__eq__("prime"):
                self.__hint_prime()
            elif __get_hint_type.__eq__("square"):
                self.__hint_square()
            elif __get_hint_type.__eq__("product"):
                self.__hint_product()

            self.__hint_types.remove(__get_hint_type)

            print(f"You Have: {self.__hint_limit} Hints Left")
            print("Guess the Number: ")
        else:
            print("No Hints Left")

    def _set_up_hints(self) -> None:
        keyboard.add_hotkey("ctrl", self._show_hints)
        keyboard.press("esc")

    def main(self) -> None:
        print("\nNote: For Hints Press \"CTRL\" on Your Keyboard. You Have 5 Hints.")

        while True:
            self._get_start_number()
            self._get_end_number()
            self._generate_random_number()
            self._set_up_hints()
            self._game_loop()

            print(f"\nWins: {self.__total_wins}, Lose: {self.__total_lose}")
            print(f"\nCurrent Win Streak: {self.__current_win_streak}, Maximum Win Streak: {self.__maximum_win_streak}")

            __play_again: str = input("\nDo You Want to Play Again? If \"Y\" for Yes, and \"N\" for No: ").lower()

            if not __play_again.__eq__("y"):
                break

            self.__reset_game_data()
