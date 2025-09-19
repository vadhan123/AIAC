def read_non_negative_number(prompt: str) -> float:
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please try again (e.g., 12 or 12.5).")


def main() -> None:
    print("\n=== Electricity Bill Calculator (with Tax) ===\n")
    units = read_non_negative_number("Enter units consumed: ")
    rate = read_non_negative_number("Enter cost per unit: ")
    tax_percent = read_non_negative_number("Enter tax percentage (e.g., 5 for 5%): ")

    subtotal = units * rate
    tax_amount = subtotal * (tax_percent / 100.0)
    total = subtotal + tax_amount

    print("\n----------- Bill Summary -----------")
    print(f"Units consumed   : {units:.2f}")
    print(f"Cost per unit    : {rate:.2f}")
    print(f"Subtotal         : {subtotal:.2f}")
    print(f"Tax (%)          : {tax_percent:.2f}%")
    print(f"Tax amount       : {tax_amount:.2f}")
    print("-----------------------------------")
    print(f"Total amount     : {total:.2f}")
    print("-----------------------------------\n")


if __name__ == "__main__":
    main()


