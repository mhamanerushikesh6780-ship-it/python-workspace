
a, b, c, d, e = 100, 100, 100, 100, 100

hotel_total = (a + b) * 1.12

flight_total = (c + d) * 1.05

cab_total = e * 1.18

total = hotel_total + flight_total + cab_total

discount = total * 0.20

final_amount = total - discount

print(f"Hotel Bill after GST = {hotel_total:.2f}")
print(f"Flight Bill after GST = {flight_total:.2f}")
print(f"Cab Bill after GST = {cab_total:.2f}")
print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {final_amount:.2f}")
