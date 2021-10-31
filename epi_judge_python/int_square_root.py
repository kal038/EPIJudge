from test_framework import generic_test


def square_root(k: int) -> int:
    l ,r = 0, k
    while l <= r:
        m = (l+r) // 2
        mid_sq = m * m
        if mid_sq == k:
            return m
        elif mid_sq > k:
            r = m  - 1
        else:
            l = m + 1
    return (l - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
