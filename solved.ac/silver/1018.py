import sys
import math


def solution(N, M, board):
    colors = ['W', 'B']
    sols = [
        [colors[0] if i == 0 else colors[1] for i in range(8)]
    ]
    
    tolerance_width_size = int(int(M - 8) / 1)  + 1
    tolerance_height_size = int(int(N - 8) / 1)  + 1
    
    for i in range(tolerance_height_size):
        for j in range(tolerance_width_size):
            can_map = board
    
    


def run():
    N, M = map(int, sys.stdin.readline().split())
    board = [str(sys.stdin.readline().strip()) for _ in range(N)]
    print("======================")
    print('\n'.join(board))
    solution(N, M, board)
    

if __name__ == "__main__":
    run()