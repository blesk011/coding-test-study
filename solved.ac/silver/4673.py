import os, sys
import argparse

db = [0] * 10001
print(len(db))
# print(len(db), len(db[0]))


def self_number(num):
    numbers = [int(n) for n in str(num)]
    total = int(num) + sum(numbers)
    return total


def solution():
    limit = 10000

    for num in range(1, 10001):
        producer = self_number(num)
        if producer <= 10000:
            db[producer] = 1

    for idx, flag in enumerate(db):
        if flag == 0 and idx != 0:
            print(idx)


def run():
    solution()



if __name__ == "__main__":
    run()