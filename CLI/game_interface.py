from abc import ABC, abstractmethod


class GameInterface(ABC):
    def __init__(self) -> None:
        pass

    # Method to get the Start Number
    @abstractmethod
    def _get_start_number(self) -> None:
        pass

    # Method to get the End Number
    @abstractmethod
    def _get_end_number(self) -> None:
        pass

    # Method to Generate the Random Number
    @abstractmethod
    def _generate_random_number(self) -> None:
        pass

    # Main Game Loop Method
    @abstractmethod
    def _game_loop(self) -> None:
        pass

    @abstractmethod
    def _check_win_condition(self, user_guess: int) -> bool:
        pass
