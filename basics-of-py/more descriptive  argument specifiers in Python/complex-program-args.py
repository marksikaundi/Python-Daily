# Certainly! Let's create a complex program that takes user input for a list of products and their prices and then generates a formatted receipt using argument specifiers. Here's the program:
def generate_receipt(products):
    total_cost = 0

    print("Receipt:")
    print("{:<20} {:<10} {:<10}".format("Product", "Price", "Quantity"))
    print("="*40)

    for product, price in products.items():
        quantity = int(input(f"Enter quantity for {product}: "))
        cost = price * quantity
        total_cost += cost
        print("{:<20} K{:<10.2f} {:<10}".format(product, price, quantity))

    print("="*40)
    print("{:<20} K{:<10.2f}".format("Total Cost:", total_cost))


def main():
    products = {
        "Item 1": 10.99,
        "Item 2": 5.49,
        "Item 3": 7.99,
    }

    generate_receipt(products)


if __name__ == "__main__":
    main()


# Explanation:

# generate_receipt is a function that takes a dictionary of products and their prices as input. It then prompts the user for the quantity of each product and calculates the cost. Finally, it prints a nicely formatted receipt.
# In the main function, we define a dictionary products containing sample product names and prices.
# We call the generate_receipt function with the products dictionary to generate the receipt.
# The program uses argument specifiers like {:<20} to specify the width of the columns and ensure proper alignment. For example, {:<20} ensures that the "Product" column is left-aligned and has a width of 20 characters.
# Prices are formatted as ${:<10.2f} to display them as kwacha(K) with two decimal places.

# Here's how the program works:

# The user is prompted to enter the quantity of each product.
# The program calculates the total cost.
# Finally, it prints a well-formatted receipt with the product names, prices, quantities, and the total cost.
# You can customize the products dictionary to include your own list of products and prices. This program demonstrates the use of argument specifiers to create a complex program with formatted output.




