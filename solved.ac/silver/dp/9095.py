from typing import List, Dict
import sys


def solution(N):
    if N == 1:
        return 1

    numbers = [1, 2, 3]
    dp = [0] * int(N+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = sum([dp[int(i-num)] for num in numbers if int(i-num) >= 0])
    
    return dp[N]


def fast_read_inputs(N):
    lines = list()
    for _ in range(N):
        lines.append(int(sys.stdin.readline()))
    
    return lines


def read_N() -> int:
    N = int(input().strip())
    return N


def run():
    N = read_N()
    cases = fast_read_inputs(N)
    for case in cases:
        print(solution(case))
    


if __name__ == "__main__":
    run()