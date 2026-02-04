"""
Create and unpack a tuple
Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
Unpack the tuple into three separate variables: lat, lon, and alt.

Create a tuple with mixed data types
Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
Unpack the tuple into three separate variables: name, age, and height.

Demonstrate tuple immutability
Create a tuple named 'immutable_tuple' with three integer values.
Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""
print("Creating and unpacking a tuple:")
coordinates = 16.7735, -3.0074, 269
lat, lon, alt = coordinates
print(lat, lon, alt)

print("\nCreating a tuple with mixed data types:")
person_info = ("Mildred", 32, 1.4)
name, age, height = person_info
print(name, age, height)

print("\nDemonstrating tuple immutability:")
immutable_tuple = 24, 7, 365
try:
    immutable_tuple[0] = 25
except TypeError as e:
    print(f"Error: {e}")