#pracs3-Q4

#Program to check voting eligibility using nested if

age = int(input("Enter your age :"))
nationality = input("Enter your nationality :")

if age >= 18:
  if nationality.lower() == "indian":
     print("Eligible to vote.")
  else:
     print("Not eligible to vote( Only Indian citizens can vote).")
else:
    print("Not eligible to vote( Age must be 18 or above).")
