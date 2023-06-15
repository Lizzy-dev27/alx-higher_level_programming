#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            return (c)

        return (c)

    else:
        return(sub(a, b))
