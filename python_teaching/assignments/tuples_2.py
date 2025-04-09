# 5. Write a program that takes a list of tuples, each containing a name and age, 
# and returns the name of the oldest person.
# Example input: [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

def find_oldest_person(people):
    if not people:
        return None  # Handle empty list
    oldest = max(people, key=lambda person: person[1])
    return oldest[0]

people_list = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

print("Oldest person:", find_oldest_person(people_list))