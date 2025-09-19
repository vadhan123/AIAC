def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Try again (e.g., 36.6).")


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    print("Temperature Converter")
    print("[1] Celsius → Fahrenheit")
    print("[2] Fahrenheit → Celsius")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        c = read_number("Enter temperature in Celsius: ")
        f = celsius_to_fahrenheit(c)
        print(f"{c:.2f} °C = {f:.2f} °F")
    elif choice == "2":
        f = read_number("Enter temperature in Fahrenheit: ")
        c = fahrenheit_to_celsius(f)
        print(f"{f:.2f} °F = {c:.2f} °C")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()


