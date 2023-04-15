print("How many points did you score")
one = float(input())
print("How many points could you have scored.")
two = float(input())
precentage = one / two
precentage = round(precentage, 4)
precentage = precentage * 100
print(f"You scored {precentage} % of the total possible points")