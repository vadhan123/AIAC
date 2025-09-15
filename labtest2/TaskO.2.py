# Function to generate multiplication tables up to n, each table up to 'upto'
def generate_tables(n, upto):
	if n <= 0 or upto <= 0:
		print("Both n and upto must be greater than 0.")
		return
	for i in range(1, n + 1):
		for j in range(1, upto + 1):
			print(f"{i} x {j} = {i * j}")


# User input section
if __name__ == "__main__":
	try:
		n = int(input("Enter the number of tables (n): "))
		upto = int(input("Enter the range for each table (upto): "))
	except ValueError:
		print("Please enter valid integer values.")
	else:
		generate_tables(n, upto)
