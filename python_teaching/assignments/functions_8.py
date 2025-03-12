# 3. Create a function that accepts only keyword-only arguments 
#    for a person's age and city, then prints them.

def details(*, age, city):
    return "Age of the person is " + age + " and city is " + city

print(details(city = "Ahmedabad", age = "23"))