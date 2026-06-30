correct_username = "admin"
correct_password = "1234"
attempt = 1
while attempt <=3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("login successful")
        break
    else:
        print("login failed try again")
        attempt += 1
        if attempt>= 3:
            print("account locked")

