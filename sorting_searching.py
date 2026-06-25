# Day 7 - Lists, Sorting, Searching, Student Marks

# Hands-on Practice
numbers = [10, 20, 30, 40]

print("Original List:", numbers)
print("First Element:", numbers[0])
print("Slicing:", numbers[1:3])

numbers.append(50)
print("After Append:", numbers)

numbers.remove(20)
print("After Remove:", numbers)

numbers.sort()
print("After Sort:", numbers)

print("\n-------------------\n")

# Coding Task - Student Marks
marks = [80, 75, 90, 85, 70]

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Student Marks")
print("Total:", total)
print("Average:", average)
print("Grade:", grade)

print("\n-------------------\n")

# Assignment - Sorting and Searching
numbers = [45, 12, 78, 23, 56]

numbers.sort()
print("Sorted List:", numbers)

search = 23

if search in numbers:
    print(search, "found in list")
else:
    print(search, "not found in list")