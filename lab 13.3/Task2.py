def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
    return None

# Test
if __name__ == "__main__":
    content = read_file("task2.py")
    if content is not None:
        print(f"File read successfully: {len(content)} characters")