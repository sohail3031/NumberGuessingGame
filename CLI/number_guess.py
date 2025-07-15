from human_player import HumanPlayer


class NumberGuess:
    def __init__(self) -> None:
        self.__game_mode: str = str()

    def main(self) -> None:
        while True:
            self.__game_mode = input("Select the Game 🎮 Mode:\n0) Quit\n1) 1 Player\n2) 2 Players\n\nEnter Your " +
                                     "Option: ")

            if self.__game_mode.__eq__("1"):
                HumanPlayer().main()
            elif self.__game_mode.__eq__("2"):
                pass
            elif self.__game_mode.__eq__("0"):
                print("Bye 👋!")

                break
            else:
                print("Invalid Option!\n")


if __name__ == "__main__":
    NumberGuess().main()
