marks = int(input("Enter Your Marks :"))

if (marks >= 90) and (marks < 100) :
    print("You Got A+ grade")

elif (marks >=80) and (marks < 90) :
    print ("You Got A grade")

elif (marks >= 65) and (marks < 80) :
    print ("You Got B grade")

elif (marks >= 35) and (marks < 65) :
    print ("You Got B grade")

else:
    print("Invalid Marks")   