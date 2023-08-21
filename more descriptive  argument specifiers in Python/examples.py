# Using String formatting (%s)
name = "Mark"
message = "Hello, %s!" % name
print(message)
# Explanation: In this example, %s is used as the placeholder for the string. When the string is formatted, %s is replaced with the value of the name variable. The output will be "Hello, Mark!"

# Integer Formatting (%d)
quantity = 5
item_price = 10
total_cost = quantity * item_price
print("Total cost is: %d Kwacha" % total_cost)
# Explanation: Here, %d is used to format the total cost, which is an integer. It substitutes %d with the value of the total_cost variable. The output will be "Total cost: 50 dollars."


# Floating-Point Formatting(%f)
pi = 3.14159265359
print("The value of pi is approximately %.2f" % pi)
# Explanation: In this case, %.2f is used to format the floating-point number pi with two digits after the decimal point. The output will be "The value of pi is approximately 3.14."


# Floating-Point Formatting with a fixed number of Digits (%<number of digits>f)
percentage = 0.7521
print("Accuracy: %.1f%%" % (percentage * 100))
# Explanation: Here, %.1f is used to format the floating-point number percentage with one digit after the decimal point. The % symbol is escaped by using %%, so it appears in the output as a percentage sign. The output will be "Accuracy: 75.2%."








