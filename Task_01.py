
a, b, c, d, e = 100, 100, 100, 100, 100

electronics_total = (a + b) * 1.18
fashion_total = (c + d) * 1.13
food_total = e * 1.07

total = electronics_total + fashion_total + food_total

discount = total * 0.20
final_bill = total - discount

print("Electronics Bill:", electronics_total)
print("Fashion Bill:", fashion_total)
print("Food Bill:", food_total)
print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
