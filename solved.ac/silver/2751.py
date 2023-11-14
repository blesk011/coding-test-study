from typing import List, Dict
import sys

def solution(lines):
    numbers = [int(line) for line in lines]
    numbers.sort()

    return numbers

def read_N() -> int:
    N = int(input().strip())
    return N

def fast_read_input():
    case = sys.stdin.readline()
    return case

def fast_read_inputs(N):
    lines = list()
    for _ in range(N):
        lines.append(sys.stdin.readline())
    
    return lines

def run():
    N = read_N()
    case = fast_read_inputs(N)
    res = solution(case)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    run()