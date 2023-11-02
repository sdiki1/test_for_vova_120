def calculate(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n % 2 == 0:
            return calculate(n // 2) + calculate(n // 2 - 1)
        else:
            return calculate(n // 2) - calculate(n // 2 - 1)


n = int(input())
result = calculate(n)
print(result)
