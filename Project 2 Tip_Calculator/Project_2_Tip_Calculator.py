print("Welcome to Tip Calculator😊")
bill=float(input("Enter the bill amount: "))
tip=float(input("Enter the tip percentage you want give: "))
persons=int(input("Enter the no. of persons: "))
share=(((bill*tip)/100)+bill)/persons
print(f"Each person should pay {share}")