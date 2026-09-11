#Smart Blood Donation System - Version 2.0
# Blood Donation System v2.0

donors = [
    ("Rahul", "A+", "Mumbai"),
    ("Priya", "B+", "Pune")
]

b = input("Blood: ").upper()
c = input("City: ").title()

for n, g, city in donors:
    if g == b and city == c:
        print("Donor:", n)
        break
else:
    print("No donor nearby")
