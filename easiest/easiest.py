"""
https://open.kattis.com/problems/easiest
"""

import sys


def sum_digits(number):
    sum_of_digits = 0
    while number:
        sum_of_digits, number = sum_of_digits + number % 10, number // 10
    return sum_of_digits


for line in sys.stdin:
    n = int(line)

    if n == 0:
        break

    p = 11
    while True:
        if sum_digits(n) == sum_digits(n * p):
            print(p)
            break
        p += 1
