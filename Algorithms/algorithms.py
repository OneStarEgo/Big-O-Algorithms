"""
Even or Odd
Given a numeric value, determine if it is even or odd.

The function should take the value in as a parameter and return a boolean value (True if even, False if odd).

Leave a comment above the function stating the time complexity.
"""

# Time complexity: O(1)
def isEven(num):
    return num % 2 == 0

print(isEven(4)) #should print True
print(isEven(7)) #should print False

# Time complexity: O(1)
def all_less_than_100(numbers):
    for num in numbers:
        if num >= 100:
            return False
    return True

print(all_less_than_100([1, 2, 3, 99])) #should print True
print(all_less_than_100([1, 2, 3, 100])) #should print False

# Time complexity: O(1)
def has_repeated_names(names):
    name_counts = {}
    for name in names:
        if name in name_counts:
            return True
        name_counts[name] = 1
    return False

print(has_repeated_names(["Joe", "Paul", "Gregor", "Ronald"])) #should print False
print(has_repeated_names(["Joe", "Ronald", "Gregor", "Joe"])) #should print True