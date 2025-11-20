from typing import Optional

class ClusterInput:
    """Class to accept user input"""

    def __init__(self, prompt: str = "Podaj liczbę klastrów: "):
        self._prompt = prompt
        self._k = None   # private field (encapsulation)

    def get_user_input(self) -> int:
        while True:
            user_input = input(self._prompt)

            try:
                number = float(user_input)  # try converting to float
            except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
                continue

            if not number.is_integer():  # check if the value is int
                print("Podaj liczbę całkowitą.")
                continue

            number = int(number)

            if number <= 0:
                print("Liczba musi być większa niż 0. Spróbuj ponownie.")
                continue

            self._k = number
            return self._k

    @property 
    def k(self) -> int:
        """Getter for accessing the number of clusters provided by the user"""
        if self._k is None:
            raise ValueError("Wartość nie została jeszcze ustawiona")
        return self._k
