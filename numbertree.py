"""
http://open.kattis.com/problems/numbertree
"""

line = input().split()

height = int(line[0])
max_node = 2**(height+1) - 1

if len(line) == 1:
    if height == 1:
        print(1)
    else:
        print(max_node)
else:
    i = 1
    for letter in line[1]:
        if letter is "R":
            i = 2 * i + 1
        else:
            i *= 2

    print(max_node - i + 1)
