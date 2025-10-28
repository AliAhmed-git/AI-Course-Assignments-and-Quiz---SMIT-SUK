a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_result = a + b
diff_result = a - b
prod_result = a * b
quot_result = a / b if b != 0 else "undefined (cannot divide by zero)"

print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Quotient: {quot_result}")
