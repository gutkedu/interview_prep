# Longest Common Subsequence

# QUESTION 1: Write a function to find the length of the longest common subsequence between two sequences.
#  E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito"
#  and its length is 7.

# A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges are some common
#  sequence types in Python.

# A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. For example,
# "edpt" is a subsequence of "serendipitous".

# ** Problem: We are given two sequences and we need to find the length of the longest common subsequence
# between them.

# ** Input: 1.A sequence e.g.'serendipitous' 2. Another sequence e.g. 'precipitation'
# ** Output: A length of the longest common subsequence e.g. 7

# Test cases

#  1.General case (string)
#  2.General case (list)
#  3.No common subsequence
#  4.One is a subsequence of the other
#  5.One sequence is empty
#  6.Both sequences are empty
#  7.Multiple subsequences with same length
#      “abcdef” and “badcfe”

T0 = {"input": {"seq1": "serendipitous", "seq2": "precipitation"}, "output": 7}

T1 = {
    "input": {"seq1": [1, 3, 5, 6, 7, 2, 5, 2, 3], "seq2": [6, 2, 4, 7, 1, 5, 6, 2, 3]},
    "output": 5,
}

T2 = {"input": {"seq1": "longest", "seq2": "stone"}, "output": 3}

T3 = {"input": {"seq1": "asdfwevad", "seq2": "opkpoiklklj"}, "output": 0}

T4 = {"input": {"seq1": "dense", "seq2": "condensed"}, "output": 5}

T5 = {"input": {"seq1": "", "seq2": "opkpoiklklj"}, "output": 0}

T6 = {"input": {"seq1": "", "seq2": ""}, "output": 0}

T7 = {"input": {"seq1": "abcdef", "seq2": "badcfe"}, "output": 3}

lcs_tests = [T0, T1, T2, T3, T4, T5, T6, T7]

