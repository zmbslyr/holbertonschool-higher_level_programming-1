#!/usr/bin/python3
for first in range(10):
    for second in range(first + 1, 10):
        print('{:d}{:d}'.format(first, second), end='')
        if first != 8 or second != 9:
            print(', ', end='')
print()
