# QUESTION 1: Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face
# down in a sequence on a table. She challenges Bob to pick out the
# card containing a given number by turning over as few cards as
# possible. Write a function to help Bob locate the card.

import jovian.pythondsa as jovian

tests = []

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# cards does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [5, 4, 3, 2, 1],
        'query': 3
    },
    'output': 2
})

tests.append({
    'input': {
        'cards': [6, 5, 4, 3, 2, 1],
        'query': 6
    },
    'output': 0
})

# Test the worst case scenario
large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}


def locate_card_linear_search(cards, query):
    """Locate a card with linear search"""
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


def test_location(cards, query, mid):
    """helper function"""
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card_binary_search(cards, query):
    """Locate card with binary search"""
    low = 0
    high = len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        #print("low:", low, "high:", high, "mid", mid)
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1

    return -1


def binary_search(lo, hi, condition):
    """generic implementation of binary search"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):
    """locate card function based on the generic implementation of binary search"""
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)


jovian.evaluate_test_cases(locate_card_linear_search, tests)
jovian.evaluate_test_cases(locate_card_binary_search, tests)
jovian.evaluate_test_cases(locate_card, tests)

result, passed, runtime = jovian.evaluate_test_case(
    locate_card_linear_search, large_test, display=False)
print("\nResult: {}\nPassed: {}\nExecution time: {} ms".format(
    result, passed, runtime))

result, passed, runtime = jovian.evaluate_test_case(
    locate_card_binary_search, large_test, display=False)
print("\nResult: {}\nPassed: {}\nExecution time: {} ms".format(
    result, passed, runtime))


# Question: Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given number.
def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)
