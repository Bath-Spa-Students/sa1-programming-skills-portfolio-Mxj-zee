secret_password = "12345"
while True:
    entered_password = input("Enter the password: ")

    if entered_password == secret_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password, please try again.")