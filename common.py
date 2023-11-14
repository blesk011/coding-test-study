from typing import List, Dict
import sys


def solution(case):
    pass

def read_input():
    case = input().strip()
    return case


def read_inputs(N: int) -> List:
    lines = list()
    for _ in range(N):
        lines.append(input().strip())

    return lines


def fast_read_input():
    case = sys.stdin.readline()
    return case


def fast_read_inputs(N):
    lines = list()
    for _ in range(N):
        lines.append(sys.stdin.readline())
    
    return lines


def read_N() -> int:
    N = int(input().strip())
    return N


def run():
    N = read_N()
    case = fast_read_inputs(N)
    print(solution(case))
    


if __name__ == "__main__":
    run()