
# 4948번

deci = int(input())

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(number+1, (number) * 2 + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(deci)
print(len(result))

