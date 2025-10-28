username_input = input("Enter username: ")
password_input = input("Enter password: ")

admin_username = "admin"
admin_password = "password123"

if(username_input == admin_username and password_input == admin_password):
    print("Login successful")
else:
    print("Login failed. Invalid username or password.")