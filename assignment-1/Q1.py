name = input("Enter name: ")
age = int(input("Enter Age: "))
percentage = float(input("Enter percentage: "))
income = float(input("Ente fmaily income: "))
is_rural = input("are you from rural area?: == (True/False): ") == "True"

if(percentage > 90) or (percentage > 85 and income < 300000):
    print("Eligibe for Scholarship")
else:
    print("Not Eligible")

    print(f"student = {name} | age = {age} | score = {percentage}%")