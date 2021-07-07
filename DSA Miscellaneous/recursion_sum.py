### sum of n numbers using recursion

def sum_recursion(n):
    if n == 0:
        return n
    else:
        return n + sum_recursion(n-1)

print(sum_recursion(15))

