signal = input("Enter traffic signal (red/yellow/green): ")

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid traffic signal")