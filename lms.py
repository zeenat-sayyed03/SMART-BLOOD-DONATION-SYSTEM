#Smart Blood Donation System - Version 1.1
donors = [
    ("Rahul", "A+"),
    ("Priya", "B+"),
    ("Amit", "O+"),
]

blood = input("Required blood group: ").upper()

matches = [name for name, group in donors if group == blood]

print("Donors:", ", ".join(matches) if matches else "No donor found")

