#!/usr/bin/python3
# 6-print_comb3.py

for i in range(100):
    if int(i / 10) != i % 10 and int(i / 10) < i % 10:
        print("{}{}".format(int(i / 10), i % 10), end="")
         if (i != 89):
             print(", ", end="")
print("")
