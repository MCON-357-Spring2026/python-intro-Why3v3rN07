"""
Dictionary of students -> grades
Print averages
"""

scores = {"bob": [90, 92, 88, 90], "fred": [64.5, 55, 0, 65], "joe": [99.5, 99.5, 99.5, 99.5]}

for name, score_list in scores.items():
    print("Name: " + name.capitalize() + " \t Average: " + str(sum(score_list)/len(score_list)))