rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter your food coset = "))
electricity = int(input("Enter your total of electricity bill = "))
charge_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in the flat = "))

total_bill = electricity * charge_unit

output = (rent + food + total_bill) / persons

print("Each person has to pay = ", output)
