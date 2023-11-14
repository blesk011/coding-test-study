from typing import List, Dict
import sys

dp = [0] * 41
one_dp = [0] * 41
zero_dp = [0] * 41

def solution(N):
    if N == 0:
        return 1, 0
    if N == 1:
        return 0, 1

    zero_dp[0] = 1
    one_dp[0] = 0
    
    zero_dp[1] = 0
    one_dp[1] = 1

    for i in range(2, N+1):
        zero_dp[i] = zero_dp[i-1] + zero_dp[i-2]
        one_dp[i] = one_dp[i-1] + one_dp[i-2]
        
    return zero_dp[N], one_dp[N]


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
        print(" ".join(map(str, solution(case))))
    


if __name__ == "__main__":
    run()