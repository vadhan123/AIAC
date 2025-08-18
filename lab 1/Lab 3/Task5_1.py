def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Try again (e.g., 36.6).")


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def main() -> None:
    c = read_number("Enter temperature in Celsius: ")
    f = celsius_to_fahrenheit(c)
    print(f"{c:.2f} °C = {f:.2f} °F")


if __name__ == "__main__":
    main()


