from typing import List, Dict
import sys
'''
시도(1)

    def solution(N):
        dp = [0] * int(N+1)

        if N == 2 or N == 3:        
            return 1
        
        for i in range(2, N+1):
            if i % 3 == 0:
                post = int(i / 3)
                dp[i] = dp[post] + 1
            elif i % 2 == 0:
                post = int(i / 2)
                dp[i] = dp[post] + 1
            else:
                dp[i] = dp[i-1] + 1
        
        print(dp)
        return dp[N]

    시도 (1)에서 문제인 점은 1을 먼저 빼고 다음 연산을 시도한 경우를 고려하지 못했음
    예를 들어, N=10인 경우에 10->9->3->1 (총 3번 연산)으로 3번만 연산을 수행하면 됨

    첨부 링크: https://jae04099.tistory.com/199
    첨부 링크를 참고하여 1을 먼저 뺀 것과, 1을 빼기전에 다른 연산을 수행한 것 중 최소 횟수인 값으로 갱신해야 한다
'''

def solution(N):
    dp = [0] * int(N+1)

    if N == 2 or N == 3:        
        return 1
    
    for i in range(2, N+1):       
        dp[i] = dp[i-1] +1 

        if i % 3 == 0:
            post = int(i / 3)
            dp[i] = min(dp[post] + 1, dp[i])
        if i % 2 == 0:
            post = int(i / 2)
            dp[i] = min(dp[post] + 1, dp[i])
    
    return dp[N]


def read_N() -> int:
    N = int(input().strip())
    return N


def run():
    N = read_N()
    print(solution(N))
    


if __name__ == "__main__":
    run()