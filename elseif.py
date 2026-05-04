kettle_boiled = input("if the kettle boiled or not (True/False)?")

if kettle_boiled:
    print("Its Done")
else:
    print("Heat it Bro")

# Even or Odd 
number = int(input("enter the number? "))
if number%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Order Cookies or samosa.

order = input("What do you want (Cookies/Samosa) ? ").lower()

if order == "cookies" or order == "samosa":
    print("Confirm the order")
else:
    print("Not Available")

size = int(input("Which size of the tea cup you want \n 1.Small \n 2.Medium \n 3.Big\n Enter the Number ? "))
if size == 1:
    print("you have selected small size so the Bill will be ₹10 ")
elif size == 2:
    print("you have selected medium size so the Bill will be ₹20 ")
elif size == 3:
    print("you have selected Big size so the Bill will be ₹30 ")
else:
    print("Not Available")

# Nested IF ELSE 

thermostat = input("is ThermoStat is active/inactive? ").lower()

if thermostat =="active":
    temp = float(input("Enter the temp of thermostat "))
    if temp > 35:
        print("High Temp")
    else:
        print("Normal Temp")
else:
    print("Thermostat is inactive")

## Ternary Operator:
bill = float(input("Enrt yhe bill amount "))
delFee = 0 if bill>3000 else 30

print(delFee)

# Match case
seat = input("Which seat you want (Normal/Luxary/Sleeper)").lower()

match seat:
    case "normal":
        print(f"Hi You have selected {seat} seat")
    case "luxary":
        print(f"Hi You have selected {seat} seat")
    case "sleeper":
        print(f"Hi You have selected {seat} seat")
    case _:
        print("its Default case")
