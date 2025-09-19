def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Try again (e.g., 36.6).")


def read_scale(prompt: str) -> str:
    valid = {"c": "C", "celsius": "C", "f": "F", "fahrenheit": "F", "k": "K", "kelvin": "K"}
    while True:
        raw = input(prompt).strip().lower()
        if raw in valid:
            return valid[raw]
        print("Invalid scale. Enter C, F, or K (or full names).")


def to_kelvin(value: float, scale: str) -> float:
    if scale == "C":
        return value + 273.15
    if scale == "F":
        return (value - 32) * 5 / 9 + 273.15
    return value


def from_kelvin(value_k: float, scale: str) -> float:
    if scale == "C":
        return value_k - 273.15
    if scale == "F":
        return (value_k - 273.15) * 9 / 5 + 32
    return value_k


def main() -> None:
    print("Temperature Converter (Celsius, Fahrenheit, Kelvin)")
    src = read_scale("From scale (C/F/K): ")
    dst = read_scale("To scale (C/F/K): ")
    temp = read_number(f"Enter temperature in {src}: ")

    temp_k = to_kelvin(temp, src)
    result = from_kelvin(temp_k, dst)

    unit_symbol = {"C": "°C", "F": "°F", "K": "K"}
    print(f"{temp:.2f} {unit_symbol[src]} = {result:.2f} {unit_symbol[dst]}")


if __name__ == "__main__":
    main()


