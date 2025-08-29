with open("input.txt", "w") as f:
    f.write("Hello\nWorld\nPython\n")
print("input.txt created with sample content.")
data = open("input.txt", "r").readlines()
with open("output.txt", "w") as output:
    for line in data:
        output.write(line.upper())
        print("Processing done")