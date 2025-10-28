a = int(input("Enter the bill amount: "))

discountPercentage = 10
spendingAmount = 1000

if a >= spendingAmount:
    discount = (discountPercentage / 100) * a
    finalAmount = a - discount
    print("You have received a discount of", discountPercentage, "%")
    print("Final bill amount after discount is:", finalAmount)
else:
    print("No discount applied. Total bill amount is:", a)