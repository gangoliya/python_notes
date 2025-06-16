# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age must be 18 or older.")

# Function to check age
def verify_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is valid. You are allowed access.")

# Main code with exception handling
try:
    user_input = int(input("Enter your age: "))
    verify_age(user_input)
except InvalidAgeError as e:
    print("Age verification failed:", e)
except ValueError:
    print("Invalid input. Please enter a numeric age.")
