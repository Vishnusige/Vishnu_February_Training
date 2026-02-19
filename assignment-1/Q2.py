name = input("Customer name: ")
price = float(input("Product price: "))

premium_input = input("Is the customer a Premium member? (yes/no): ")
is_premium = premium_input.lower() == "yes"
coupon = input("Coupon code: ")
discount = 0.0

#Discounts

if price > 5000 and is_premium:
 discount = price * 0.20

elif is_premium or coupon == "SAVE10":
 discount = price * 0.10

#Printing the Bill

print("-----Bill Details-----")
print("Customer: ",name)
print("Original price: ",price)
print("Discount applied: ",discount)
print("Final_price: ",price - discount)

if is_premium:
 print("Premium benefits applied")



