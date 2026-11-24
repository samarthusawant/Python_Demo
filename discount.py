role =input("Enter Your Role")

age = int(input("Enter Your Age"))

discount= (age <= 21 and role == 'Student')

print ("Eligible :", discount)
