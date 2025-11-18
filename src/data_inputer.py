def get_user_input(prompt: str = "Podaj liczbę klastrów: ") -> int:
    while True:
        user_input = input(prompt)

        # Sprawdzenie czy to liczba
        if not user_input.isdigit():
            print("To nie jest liczba. Spróbuj ponownie.")
            continue

        value = int(user_input)

        if value <= 0:
            print("Liczba musi być większa niż 0. Spróbuj ponownie.")
        else:
            return value
