from typing import List, Dict
import sys

dp =  [[0] * 1001] * 3

def solution(case):
    N = len(case)
    for costs in case:
        pass



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