"""
1. Create a list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with a loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is the length of the corresponding food item in the original list.
"""

foods = ["mango", "musubi", "malasadas"]
print(foods[0], foods[-1])

foods.remove("malasadas")
foods.append("mochi")

print("\nFoods:")
for food in foods:
    print(food)

name_lengths = [len(food) for food in foods]
print("\nName lengths:")
print(name_lengths)