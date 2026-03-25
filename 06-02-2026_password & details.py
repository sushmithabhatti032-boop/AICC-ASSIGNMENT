<<<<<<< HEAD
# Assignment - 06/02/2026

# Print personal details
print("Name: Sushmitha")
print("Favorite Food: Biryani")
print("Dream Company: Google")

print("-------------------")

# Password Authentication
password = input("Create password: ")

if len(password) >= 8:
    print("Password created successfully")
else:
    print("Password must be at least 8 characters")

login = input("Enter password: ")

if login == password:
    print("Access Granted")
else:
=======
# Assignment - 06/02/2026

# Print personal details
print("Name: Sushmitha")
print("Favorite Food: Biryani")
print("Dream Company: Google")

print("-------------------")

# Password Authentication
password = input("Create password: ")

if len(password) >= 8:
    print("Password created successfully")
else:
    print("Password must be at least 8 characters")

login = input("Enter password: ")

if login == password:
    print("Access Granted")
else:
>>>>>>> fc53bf64516712dc26054b59234aa96adbd40a04
    print("Access Denied / Wrong Password")