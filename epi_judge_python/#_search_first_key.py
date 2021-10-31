from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    l = 0
    r = len(A) - 1
    result = -1
    while l <= r:
        mid = (l+r) // 2
        if A[mid] == k:
            # we can't stop just yet because we are not sure this is the first occurence
            result = mid
            r = mid - 1 # eliminate the whole array to the right since the array is sorted in non-decreasingn order
        elif A[mid] > k:
            r = mid - 1
        else:
            l = mid + 1
    return result 



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
