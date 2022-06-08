
# You are given list of numbers, obtained by rotating a sorted list an
# unknown number of times. Write a function to determine the minimum number
# of times the original sorted list was rotated to obtain the given list.
# Your function should have the worst-case complexity of O(log N), where N
# is the length of the list. You can assume that all the numbers in the
# list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the
# sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# We define "rotating a list" as removing the last element of the list and
# adding it before the first element. E.g. rotating the list [3, 2, 4, 1]
# produces [1, 3, 2, 4].

# "Sorted list" refers to a list where the elements are arranged in the
# increasing order e.g. [1, 3, 5, 7].

# The method:
# 1. State the problem clearly. Identify the input & output formats.

# Q: Express the problem in your own words below
# O problema pede para escrever uma função para determinar o numero minimo de
# vezes que uma lista em ordem foi rotacionada.

# Q: The function you write will take one input called nums. What does it
# represent? Give an example.
# Represent a sorted rotated list, nums = [5,6,1,2,3,4]

# Q: The function you write will return a single output called rotations.
# What does it represent? Give an example.
# Represent the number of rotations that the sorted list had: rotations = 2

import jovian.pythondsa as jovian
from jovian.pythondsa import binary_search

# 2. Come up with some example inputs & outputs. Try to cover all edge cases.

tests = []

tests.append({
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 8, 1, 14],
    },
    'output': 3
})

tests.append({
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3],
    },
    'output': 5
})

tests.append({
    'input': {
        'nums': [1, 2, 3, 4, 5],
    },
    'output': 0
})

tests.append({
    'input': {
        'nums': [5, 1, 2, 3, 4],
    },
    'output': 1
})

tests.append({
    'input': {
        'nums': [],
    },
    'output': 0
})

tests.append({
    'input': {
        'nums': [1],
    },
    'output': 0
})

# 3. Come up with a correct solution for the problem. State it in plain English.
# If a sorted number is rotated k times, then the smallest number in the list
# end up at position k (counting from 0).

# We can use the linear search algorithm as a first attempt to solve this
# problem i.e. we can perform the check for every position one by one. But
# first, try describing the above solution in your own words, that make it
# clear to you.

# Q (Optional): Describe the linear search solution explained above problem
# in your own words.

# 1- Create a variable position with value 0
# 2 - compare the number at current position to the number before it
# 3 - if the number is smaller than its predecessor, then return position
# 4- Otherwise, increment position and repeat till we exhaust all the numbers


# 4. Implement the solution and test it using example inputs. Fix bugs, if any.

def count_rotations_linear(nums: list):
    """CountRotations using linear search"""
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position += 1
    return 0


jovian.evaluate_test_cases(count_rotations_linear, tests)

# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# Q: What is the worst-case complexity (running time) of the algorithm expressed
# in the Big O Notation? Assume that the size of the list is N (uppercase).
# R: O(N) (Linear)

# 6. Apply the right technique to overcome the inefficiency.
# Repeat steps 3 to 6.
# Applying binary search... If the middle element is smaller than its
# predecessor, then it is the answer. If isnt this check is not sufficient to
# determine whether the answer lies to the left or the right of it

# [7, 8, 1, 3, 4, 5, 6] (answer lies to the left of the middle element)
# [1, 2, 3, 4, 5, -1, 0] (answer lies to the right of the middle element)

# If the middle element of the list is smaller than the last element of the
# range, then the answer lies to the left of it, otherwise to the right.

# 7. Come up with a correct solution for the problem. State it in plain English.

# Q (Optional): Describe the binary search solution explained above problem
# in your own words.

# 1. Create a variable position at 0, low and high = len(list-1)
# 2. Find the middle element of the list using low and high variables
# 3. Compare the middle element to the last element of the list, checking if it
# is smaller than
# 4. If its smaller, the solution is on the right, otherwise left

# 8. Implement the solution and test it using example inputs. Fix bugs, if any.


def count_rotations_binary(nums: list):
    """Counts the number of rotations using binary search"""
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        print("lo:", lo, ", hi:", hi, ", mid:",
              mid, ", mid_number:", mid_number)
        if mid > 0 and nums[mid] < nums[mid-1]:
            return mid
        elif nums[mid] < nums[hi]:
            hi = mid - 1
        else:
            lo = mid + 1
    return 0


jovian.evaluate_test_cases(count_rotations_binary, tests)


def count_rotations_generic(nums):
    def condition(mid):
        pass  # replace this with your code
    return binary_search(0, len(nums)-1, condition)
