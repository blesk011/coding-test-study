from typing import List, Dict
import sys

'''
 기본적인 DP 문제로 볼 수 있음. 
 F(N) = min( F(N-3) + 1, F(N-5) + 1)
 위와 같이 점화식을 구성하여, 3kg, 5kg를 하나 취했을때 남은 kg에 대해서 구할 수 있는 최소 봉지 개수가 있다면
 그 갯수가 N일때의 최소 봉지 개수임

 이 문제에서는 일반항에 대한 예외처리를 생각하는 것이 문제 해결을 위해서 필요한 부분이라고 보임

 - 추가
    다른 블로그에서는 DP외에 greedy 방식으로 푸는 방법도 소개되어 있어,
    해당 방식으로도 해결해보면 생각의 폭을 넓힐 수 있을것으로 생각함
    
    recursive: https://howudong.tistory.com/37

 - 4년전에 내가 푼 풀이
    N = int(input())
    cnt = 0
    none = -1
    while True:
            if N%5 == 0:
                    print(int(N/5) + cnt)
                    break
            else:
                    N = N-3
                    cnt = cnt + 1
                    if N < 0:
                            print(none)
                            break
                    elif N == 0:
                            print(cnt)
                            break
'''

dp = [0] * 5001
dp[3] = 1
dp[5] = 1

'''
가능한 경우의 수
1) 5만 사용하는 경우 - 우선 순위 1
2) 5, 3을 같이 사용하는 경우 
3) 3만 사용하는 경우
4) 만들어질 수 없는 경우

'''

def solution(N):
    if N == 3 or N == 5:
        return 1
    
    for i in range(6, N+1):
        if dp[i-5]: # 마지막에 5가 추가된다
            dp[i] = dp[i-5] + 1
        elif dp[i-3]:
            dp[i] = dp[i-3] + 1
        elif dp[i-5] and dp[i-3]:
            dp[i] = min(dp[i-3], dp[i-5]) + 1        

    if dp[N] == 0:
        return -1
    else:
        return dp[N]


def read_N() -> int:
    N = int(input().strip())
    return N


def run():
    N = read_N()
    print(solution(N))
    


if __name__ == "__main__":
    run()