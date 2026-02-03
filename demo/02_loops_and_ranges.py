#Basic loop and range examples in Python.

def line():
    print("---")

#print numbers from 0 to 4
for i in range(5):
    print(i)
line()

#print numbers from 2 to 7
for i in range(2, 8):
    print(i)
line()

#print numbers from 3 to 14 with a step of 3
for i in range(3, 15, 3):
    print(i)
line()

#print numbers from 10 down to 2 with a step of -2
for i in range(10, 0, -2):
    print(i)
line()

#print numbers from 1 to 9 with a step of 2
for i in range(1, 10, 2):
    print(i)
line()

#Countdown from 3 to 1 using a while loop
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1
line()

#print even numbers from 0 to 10 using while loop
num = 0
while num <= 10:
    if num % 2 == 0:
        print("Even number:", num)
    num += 1
line()

#example of do-while loop using while True
n = 1
while True:
    print("Number:", n)
    n += 1
    if n > 5:
        break
line()

#basic common for loop iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
