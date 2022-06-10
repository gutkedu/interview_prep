# Problem

# QUESTION 1: You're working on a new feature on Jovian called "Top Notebooks of
# the Week". Write a function to sort a list of notebooks in decreasing
# order of likes. Keep in mind that up to millions of notebooks can be created
# every week, so your function needs to be as efficient as possible.

# The problem of sorting a list of objects comes up over and over in computer
# science and software development, and it's important to understand common
# approaches for sorting, and the trade-offs they offer. Before we solve the
# above problem, we'll solve a simplified version of the problem:

# QUESTION 2: Write a program to sort a list of numbers.

# "Sorting" usually refers to "sorting in ascending order", unless specified
# otherwise.

# 1. State the problem clearly. Identify the input & output formats.
# Problem

#    We need to write a function to sort a list of numbers in increasing order.
# Input
#    nums: A list of numbers e.g. [4, 2, 6, 3, 4, 6, 2, 1]
# Output
#    sorted_nums: The sorted version of nums e.g. [1, 2, 2, 3, 4, 4, 6, 6]
# The signature of our function would be as follows:

# 2. Come up with some example inputs & outputs.

import numbers
import random
import jovian.pythondsa as jovian

# List of numbers in random order
test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}

# List of numbers in random order
test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}

# A list that's already sorted
test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list that's sorted in descending order
test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list containing repeating elements
test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

# An empty list
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}

# A list containing just one element
test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

# A list containing one element repeated many times
test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}


in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

# 3. Come up with a correct solution. State it in plain English.

# It's easy to come up with a correct solution. Here's one:

#  1.Iterate over the list of numbers, starting from the left
#  2.Compare each number with the number that follows it
#  3.If the number is greater than the one that follows it, swap the two elements
#  4.Repeat steps 1 to 3 till the list is sorted.

# We need to repeat steps 1 to 3 at most n-1 times to ensure that the array is
# sorted. Can you explain why? Hint: After one iteration, the largest number
# in the list.

# This method is called bubble sort, as it causes smaller elements to bubble to
# the top and larger to sink to the bottom. Here's a visual
# representation of the process:

# 4. Implement the solution and test it using example inputs.


def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)

    # 4.Repeat the process n-1 times
    for _ in range(len(nums)-1):
        # 1. Iterate over the array (except for the last element)
        for i in range(len(nums) - 1):
            # 2.Compare the number with
            if nums[i] > nums[i+1]:
                # 3.Swap the elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


# jovian.evaluate_test_cases(bubble_sort, tests)

# 5. Analyze the algorithm's complexity and identify inefficiencies

# There are two loops, each of length n-1, where n is the number of elements in
# nums. So the total number of comparisons is (n−1)∗(n−1) i.e. (n−1)2 i.e. n2−2n+1

# Expressing this in the Big O notation, we can conclude that the time complexity
#  of bubble sort is O(n2) (also known as quadratic complexity).

# Insertion Sort


def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums


# jovian.evaluate_test_cases(insertion_sort, tests)

# 6. Apply the right technique to overcome the inefficiency. Repeat Steps 3 to 6.

# To performing sorting more efficiently, we'll apply a strategy called Divide
# and Conquer, which has the following general steps:

#   1. Divide the inputs into two roughly equal parts.
#   2. Recursively solve the problem individually for each of the two parts.
#   3. Combine the results to solve the problem for the original inputs.
#   4. Include terminating conditions for small or indivisible inputs.

# Merge Sort - divide and conquer to sorting problems


# 7. Come up with a correct solution. State it in Plain English.

# Here's a step-by-step description for merge sort:

#  1.  If the input list is empty or contains just one element, it is already
# sorted. Return it.
#  2.  If not, divide the list of numbers into two roughly equal parts.
#  3.  Sort each part recursively using the merge sort algorithm. You'll get
# back two sorted lists.
#  4.  Merge the two sorted lists to get a single sorted list

# Can you guess how the "merge" operation step 4 works? Hint: Watch this
# animation: https://youtu.be/GW0USDwhBgo?t=28

# QUESTION 3: Write a function to merge two sorted arrays.

# Try to explain how the merge operation works in your own words below:


def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    # Get the midpoint
    mid = len(nums) // 2
    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    # Combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)
    return sorted_nums


def merge(nums1, nums2):
    # list to store the results
    merged = []
    # incides for iteration
    i, j = 0, 0
    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):
        # Include the smaller element in the result and move to the next element
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    # Return the final merged array
    return merged + nums1_tail + nums2_tail


#print(merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12]))

#jovian.evaluate_test_cases(merge_sort, tests)


# 9. Analyze the algorithm's complexity and identify inefficiencies

# The time complexity of the merge sort algorithms is O(nlogn).

# 10. Apply the right technique to overcome the inefficiency.
# Repeat Steps 3 to 6.

# The fact that merge sort requires allocating additional space as large as the
# input itself makes it somewhat slow in practice because memory allocation is
# far more expensive than comparisons or swapping.

# Quicksort

# To overcome the space inefficiencies of merge sort, we'll study another
# divide-and-conquer based sorting algorithm called quicksort,
# which works as follows:

# 1. If the list is empty or has just one element, return it. It's already
# sorted.
# 2. Pick a random (or last, first...) element from the list. This element is
# called a pivot.
# 3. Reorder the list so that all elements with values less than or equal to
# the pivot come before the pivot, while all elements with values greater than
# the pivot come after it. This operation is called partitioning.
#  4. The pivot element divides the array into two parts which can be sorted
# independently by making a recursive call to quicksort.

def quicksort(nums, start=0, end=None):
    #print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)  # Done one time only, to not modify input list
        end = len(nums) - 1  # Set end to the final element of the list
    # if the list has at least two elements
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)
    return nums


def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    left, right = start, end-1
    while right > left:
        # Increment left pointer if number is less or equal to pivot
        if nums[left] <= nums[end]:
            left += 1
        # Decrement right pointer if number is greater than pivot
        elif nums[right] > nums[end]:
            right -= 1
        # Two out-of-place elements found, swap them
        else:
            nums[left], nums[right] = nums[right], nums[left]
    # Place the pivot between the two parts
    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left]
        return left
    else:
        return end


#jovian.evaluate_test_cases(quicksort, tests)


# Analyze the algorithm's complexity and identify inefficiencies

# The average case complexity of the quick sort algorithm is O(nlog(n)), while
# the worst case complexity is O(n^2)

# Let's return to our original problem statement now.

# QUESTION 1: You're working on a new feature on Jovian called "Top Notebooks
# of the Week". Write a function to sort a list of notebooks in decreasing
# order of likes. Keep in mind that up to millions of notebooks can be created
# every week, so your function needs to be as efficient as possible.

# First, we need to sort objects, not just numbers. Also, we want to sort them in
# the descending order of likes. To achieve this, all we need is a custom
# comparison function to compare two notebooks.

class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)


# Test cases
nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)
notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]


def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'


def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'


def merge_sort_2(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge_2(merge_sort_2(objs[:mid], compare),
                   merge_sort_2(objs[mid:], compare),
                   compare)


def merge_2(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


#sorted_notebooks = merge_sort_2(notebooks, compare_likes)
# print(sorted_notebooks)

def compare_titles(nb1, nb2):
    if nb1.title < nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    elif nb1.title > nb2.title:
        return 'greater'
