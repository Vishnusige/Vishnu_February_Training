stored_user = "Vishnu_AI"
stored_password = "Mentorgem7"
is_active = False

#Login Credentials
entered_user = input("Enter Username: ")
entered_pass = input("Enter Password: ")

#Authentication
if entered_user == stored_user and entered_pass == stored_password and is_active:
    print("Login Successful")
elif not is_active and entered_user == stored_user and entered_pass == stored_password:
    print("Account Disabled")
else:
    print("Wrong Credentias")