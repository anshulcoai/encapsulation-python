class Product:
    def __init__(self, name, quantity=0, price_per_unit=0):
        self.__name = name
        self.__quantity = max(0, quantity)  # Ensure non-negative
        self.__price_per_unit = max(0, price_per_unit)  # Ensure non-negative

    # Getter for name
    def get_name(self):
        return self.__name

    # Getter for quantity
    def get_quantity(self):
        return self.__quantity

    # Getter for price per unit
    def get_price_per_unit(self):
        return self.__price_per_unit

    # Setter for quantity with validation
    def restock(self, amount):
        if amount < 0:
            print("Error: Restock amount cannot be negative.")
        else:
            self.__quantity += amount
            print(f"{amount} units added. New quantity: {self.__quantity}.")

    # Setter for price per unit with validation
    def set_price_per_unit(self, price):
        if price < 0:
            print("Error: Price per unit cannot be negative.")
        else:
            self.__price_per_unit = price
            print(f"Price per unit updated to: {self.__price_per_unit}.")

    # Calculate the total value of the product
    def calculate_total_value(self):
        return self.__quantity * self.__price_per_unit

# Example usage
product = Product("Laptop", 10, 50000)
print(f"Product: {product.get_name()}")
print(f"Quantity: {product.get_quantity()}")
print(f"Price per unit: {product.get_price_per_unit()}")

product.restock(5)
product.set_price_per_unit(52000)
print(f"Total value of stock: {product.calculate_total_value()}")

product.restock(-3)  # This will trigger an error
product.set_price_per_unit(-1000)  # This will trigger an error
