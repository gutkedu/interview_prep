# Problem Statement - Polynomial Multiplication

# Given two polynomials represented by two lists, write a function that
# efficiently multiplies given two polynomials. For example, the lists
# [2, 0, 5, 7] and [3, 4, 2] represent the polynomials \(2 + 5x^2 + 7x^3\)
#  and \(3 + 4x + 2x^2\).

# Their product is

# \((2 \times 3) + (2 \times 4 + 0 \times 3)x + (2 \times 2 + 3 \times 5 + 4
# \times 0)x^2 + (7 \times 3 + 5 \times 4 + 0 \times 2)x^3 + (7 \times 4 + 5
# \times 2)x^4 + (7 \times 2)x^5\) i.e.

# \(6 + 8x + 19x^2 + 41x^3 + 38x^4 + 14x^5\)

# It can be represented by the list [6, 8, 19, 41, 38, 14].

# Solution

# 1. State the problem clearly. Identify the input & output formats.
# Input

# A list of numbers representing a polynomial
# A list of numbers representing a polynomial
# Output

# A list of number representing the multiplication of the inputs polynomials

# 2. Come up with some example inputs & outputs. Try to cover all edge cases.

import jovian.pythondsa as jovian


test0 = {
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [3, 4, 2]
    },
    'output': [6, 8, 19, 41, 38, 14]
}

test1 = {
    'input': {
        'poly1': [10, -1, 3],
        'poly2': [2, 1]
    },
    'output': [20, 8, 5, 3]
}

test2 = {
    'input': {
        'poly1': [3, 2],
        'poly2': [-7, 1]
    },
    'output': [-21, -11, 2]
}

tests = [test0, test1, test2]

# 3. Come up with a correct solution for the problem. State it in plain English.

# Here's the simplest solution: If you have lists poly1 and poly2 representing
# polynomials of length m and n respectively, the highest degree of the exponents
# are m−1 and n−1 respectively. Their product has the degree (m−1)+(n−1) i.e
# m+n−2. The list representing the product has the length m+n−1. So, we can
# create a list result of length m+n−1 and set
# result[k] = Sum of all the pairs poly1[i] * poly2[j] where i+j = k

# result[k] = Sum of all the pairs poly1[i] * poly2[j] where i+j = k


def multiply_basic(poly1, poly2):
    size_poly1, size_poly2 = len(poly1), len(poly2)
    prod = [0] * (size_poly1 + size_poly2 - 1)
    for i in range(size_poly1):
        for j in range(size_poly2):
            prod[i+j] += poly1[i] * poly2[j]
            print(prod)
    return prod


jovian.evaluate_test_cases(multiply_basic, tests)
