reqAge = 13
appName = "Cool Social Media App"
print("How old are you?")
age = input()
if int(age) >= int(reqAge):
    print("welcome to " + appName)
else:
    print(f"You must be {reqAge} or older to use this app.")