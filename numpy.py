import numpy as np

# Marks of 5 subjects
marks = np.array([85, 78, 82, 88, 90])

print("My marks are:", marks)

# Basic calculations
total = np.sum(marks)
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

print("Total marks:", total)
print("Average marks:", average)
print("Highest marks:", highest)
print("Lowest marks:", lowest)

# Find subjects where marks are above 80
above_80 = marks > 80

print("Marks above 80:", marks[above_80])