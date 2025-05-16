# Implement a class Student that stores a student's name and a list of marks. 
# Add a method average() that returns the average marks. 
# Create an object and calculate the average for marks [85, 90, 78].

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        if len(self.marks) == 0:
            return 0
        return round(sum(self.marks) / len(self.marks), 2)

# Create an object of Student with marks [85, 90, 78]
student = Student("John Doe", [85, 90, 78])

# Print the average marks
print("Average Marks:", student.average())
