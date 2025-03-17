import sys
sys.setrecursionlimit(10000)

N = int(input())

canvas = [[' ' for _ in range(2 * N - 1)] for _ in range(N)]

def draw_triangle(n, r, c):
    if n == 3:
        canvas[r][c] = '*'
        canvas[r+1][c-1] = '*'
        canvas[r+1][c+1] = '*'
        for i in range(-2, 3):
            canvas[r+2][c+i] = '*'
        return
    
    # 위쪽 삼각형
    draw_triangle(n // 2, r, c)
    # 왼쪽 아래 삼각형
    draw_triangle(n // 2, r + n // 2, c - n // 2)
    # 오른쪽 아래 삼각형
    draw_triangle(n // 2, r + n // 2, c + n // 2)

draw_triangle(N, 0, N - 1)

for row in canvas:
    print(''.join(row))