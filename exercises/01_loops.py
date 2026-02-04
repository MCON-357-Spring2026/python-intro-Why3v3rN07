"""
1. Print numbers from 1 to 10
2. Print even numbers from 1 to 20
3. Calculate the sum of numbers from 1 to 100
4. Print the multiplication table of 5

"""
print("numbers 1-10:")
for i in range(1, 11):
    print(i)

print("\neven numbers from 1 to 20:")
for i in range(2, 20, 2):
    print(i)

print("\nsum of numbers from 1 to 100:")
print(sum(range(1, 101)))

print("\nmultiplication table of 5:")
print([i*5 for i in range(14)])