#Smart Blood Donation System - Version 1.0
donors = {"A+": "Rahul", "B+": "Priya", "O+": "Amit"}

blood = input("Enter blood group: ").upper()

if blood in donors:
    print("Donor:", donors[blood])
else:
    print("No donor available")
