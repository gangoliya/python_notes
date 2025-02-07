role = "admin" 
membership = "premium" 
age = 17 

if (role == "admin" or membership == "premium") and not age < 18: 
    print("Access Granted")
else: 
    print("Access Denied")