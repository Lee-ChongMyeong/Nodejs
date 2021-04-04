import sys

n = int(sys.stdin.readline())

memo = {
    1 : 1,
    2 : 2
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n] % 15746

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo % 15746


print(fibo_dynamic_programming(n, memo))

# N = 1 (1)

# N = 2 (2)

# N = 3 (3)
# 001, 100, 111

# N = 4 (5)
# 0000, 0011, 1001, 1100, 1111

# N = 5 (8)
# 00111, 10011, 11001, 11100
# 00001, 00100, 10000, 11111



