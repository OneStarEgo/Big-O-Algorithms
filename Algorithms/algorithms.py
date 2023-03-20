
# Time complexity: O(1) - Linear
def isEven(num):
    return num % 2 == 0

print(isEven(4)) #should print True
print(isEven(7)) #should print False

# Time complexity: O(1) - Linear
def all_less_than_100(numbers):
    for num in numbers:
        if num >= 100:
            return False
    return True

print(all_less_than_100([1, 2, 3, 99])) #should print True
print(all_less_than_100([1, 2, 3, 100])) #should print False

# Time complexity: O(1) - Linear
def has_repeated_names(names):
    name_counts = {}
    for name in names:
        if name in name_counts:
            return True
        name_counts[name] = 1
    return False

print(has_repeated_names(["Joe", "Paul", "Gregor", "Ronald"])) #should print False
print(has_repeated_names(["Joe", "Ronald", "Gregor", "Joe"])) #should print True

# Time complexity: O(n^2) - Quadratic
def sort_list(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

unsorted = [6, 8, 3, 4, 7, 2]
sorted = sort_list(unsorted)

print(sorted) #should print [2, 3, 4, 6, 7, 8]