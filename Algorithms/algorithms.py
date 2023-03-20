"""
Even or Odd
Given a numeric value, determine if it is even or odd.

The function should take the value in as a parameter and return a boolean value (True if even, False if odd).

Leave a comment above the function stating the time complexity.
"""

# Time complexity: O(1)
def isEven(num):
    return num % 2 == 0

print(isEven(4))
print(isEven(7))
