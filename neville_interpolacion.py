import tkinter as tk

def neville_interpolacion (x, y, target):
    n = len(x)
    Q = [[0] * n for _ in range(n)]

    for i in range(n):
            Q[i][0] = y [i]
    
    for i in range (1, n):
        for j in range (1, i + 1):
            Q[i][j] = ((target - x [i - j]) * Q [i][j - 1] -(target -x[i]) * Q[i - 1]) / (x[i] - x[i -j])

    return Q [n - 1][n - 1]
    
