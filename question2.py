name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
tickets = int(input("Enter Number of Tickets: "))
if age < 12:
    price_per_ticket = 120
elif age >= 12 and age <= 59:
    price_per_ticket = 200
else:  
    price_per_ticket = 150
total_before = price_per_ticket * tickets
if tickets >= 5:
    discount = total_before * 0.10
else:
    discount = 0
final_amount = total_before - discount
print("Customer Name:", name)
print("Ticket Price: Rs", price_per_ticket)
print("Number of Tickets:", tickets)
print("Total Before Discount: Rs", total_before)
print("Discount: Rs", int(discount))
print("Final Amount: Rs", int(final_amount))