# 9461

# p(1) = 1
# p(2) = 1
# p(3) = 1
# p(4) = 2      
# p(5) = 2
# ===============
# p(6) = 3   *  
# p(7) = 4
# p(8) = 5
# p(9) = 7
# p(10) = 9  *
# p(11) = 12 **     p(11) = p(10) + p(6)
# p(12) = 16
# p(13) = 21
# p(14) = 28
# p(15) = 28 + 9 = 37   p(15) = p(14) + p(10)

# ==>  p(n) = p(n-1) + p(n-5)

memo = {
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 2,
    5 : 2
    11 : ? 
}
            11 
def triangle(n, triangle_memo):
    

    if n in triangle_memo:
        return triangle_memo[n]

    nth_triangle = triangle(n - 1, triangle_memo) + triangle(n - 5, triangle_memo)
    triangle_memo[n] = nth_triangle
    return nth_triangle


ready = int(input())

for i in range(ready):

    number = int(input())

    print(triangle(number, memo))


