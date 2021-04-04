# 2869

a, b, v = map(int, input().split())

k = (v - b) / ( a -b )

print(int(k) if k == int(k) else int(k + 1))

# [true_value] if [condition] else [false_value] // 파이썬 지원