def rectangle_area(x, y):
    return x * y
def square_area(x, y=0):
    return x * x
def circle_area(x, y=0):
    return 3.14 * x * x
def calculate_area(shape, x, y=0):
    area_funcs = {
        "rectangle": rectangle_area,
        "square": square_area,
        "circle": circle_area
    }
    func = area_funcs.get(shape)
    if func:
        return func(x, y)
    else:
        raise ValueError(f"Unknown shape: {shape}")
print(f"Rectangle area: {calculate_area('rectangle', 5, 3)}")
print(f"Square area: {calculate_area('square', 4)}")
print(f"Circle area: {calculate_area('circle', 2)}")