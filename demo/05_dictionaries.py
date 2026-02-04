# This script demonstrates basic dictionary operations in Python.
student = {"name": "Alice", "age": 21}
student["gpa"] = 3.8

# Accessing values
for k, v in student.items():
    print(k, v)

# Updating values
student["age"] = 22
print("Updated age:", student["age"])

# Deleting a key-value pair
del student["gpa"]
print("After deleting gpa:", student)

# Checking for key existence
if "name" in student:
    print("Name exists in student dictionary.")

# Using get method to avoid KeyError
gpa = student.get("gpa", "Not Available")
print("GPA:", gpa)

# Iterating over keys
for key in student.keys():
    print("Key:", key)

# Iterating over values
for value in student.values():
    print("Value:", value)

# Nested dictionary
courses = {"Math": {"credits": 3, "grade": "A"},
"Science": {"credits": 4, "grade": "B"}}
print("Courses:", courses)

# Adding a new course
courses["History"] = {"credits": 3, "grade": "A-"}
print("After adding History course:", courses)

# Removing a course
courses.pop("Science")
print("After removing Science course:", courses)

# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(5)}
print("Squared numbers:", squared_numbers)

# Merging dictionaries
additional_info = {"major": "Computer Science", "graduation_year": 2023}
student.update(additional_info)
print("After merging additional info:", student)

# Clearing the dictionary
student.clear()
print("After clearing student dictionary:", student)

# Using defaultdict from collections module (sets default key datatype)
from collections import defaultdict
grades = defaultdict(list)
grades["Alice"].append("A")
grades["Bob"].append("B")
print("Grades:", dict(grades))

# Using Counter from collections module (counts occurrences)
from collections import Counter
word_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(word_list)
print("Word count:", word_count)
