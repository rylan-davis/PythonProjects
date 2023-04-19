age = input("How old are you: ")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You may enter, but you need a wristband.")
    elif age >= 21:
        print("You can enter without a wristband.")
    else:
        print("You are to young to enter.")
else:
    print("Please enter an age")