class ShoppingCart:
	def __init__(self):
		self.items = []  # Each item: dict with name, price, qty
		self.discount_percent = 0
		self.discount_applied = False

	def add_item(self, name, price, qty):
		self.items.append({"name": name, "price": price, "qty": qty})
	def apply_discount(self, percent):
		if self.discount_applied:
			return  # Discount can only be applied once
		if percent < 0:
			percent = 0
		self.discount_percent = percent
		self.discount_applied = True
	def total(self):
		subtotal = sum(item["price"] * item["qty"] for item in self.items)
		if self.discount_applied and self.discount_percent > 0:
			discount = int(subtotal * (self.discount_percent / 100))
			return int(subtotal - discount)
		return int(subtotal)
if __name__ == "__main__":
	cart = ShoppingCart()
	while True:
		name = input("Enter item name (or 'done' to finish): ")
		if name.lower() == 'done':
			break
		try:
			price = float(input("Enter price: "))
			qty = int(input("Enter quantity: "))
		except ValueError:
			print("Invalid input. Please enter numeric values for price and quantity.")
			continue
		cart.add_item(name, price, qty)
	try:
		discount = float(input("Enter discount percent (0 if none): "))
	except ValueError:
		discount = 0
	cart.apply_discount(discount)
	print("Total:", cart.total())
