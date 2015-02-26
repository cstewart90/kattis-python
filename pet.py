"""
https://open.kattis.com/problems/pet
"""

import sys

max_points = 0
winner = 0
for x in range(1, 6):
    line = sys.stdin
    grades = list(map(int, input().split()))

    points = sum(grades)
    if points > max_points:
        max_points = points
        winner = x

print("{} {}".format(winner, max_points))
