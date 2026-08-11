hours = int(input("Enter parking hours: "))
if hours <= 2:
    charge = hours * 30
elif hours >= 3 and hours <= 5:
    charge = hours * 25
else:  # more than 5 hours
    charge = hours * 20
if charge > 150:
    service_charge = 20
else:
    service_charge = 0
final_amount = charge + service_charge
print("Parking Charge: Rs", charge)
print("Service Charge: Rs", service_charge)
print("Final Amount: Rs", final_amount)