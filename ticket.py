age = int(input("Enter Your age :"))
ticket_price = 500
if age <= 12:
    print(f"You got 10% Discount On Ticket Price is {ticket_price - (ticket_price/100)*10}")

else:
    print(f"Your Ticket Price is :{ticket_price}")
