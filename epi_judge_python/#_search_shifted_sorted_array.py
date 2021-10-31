from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    l = 0
    r = len(A) - 1
    while l < r:
        m = (l+r) // 2
        if A[m] > A[r]:
            l = m + 1
        else:
            r = m
    return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
