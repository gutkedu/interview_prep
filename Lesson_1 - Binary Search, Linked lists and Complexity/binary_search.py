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
        mid_number = cards[mid]

        print("low:", low, "high:", high, "mid", mid, "mid_number", mid_number)

        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1

    return -1


jovian.evaluate_test_cases(locate_card_linear_search, tests)
jovian.evaluate_test_cases(locate_card_binary_search, tests)