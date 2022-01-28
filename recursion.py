def factorial(n: int):
    """
    Base condition
    Without the base condition, we will get
    RecursionError
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


num = 3
print(f"The factorial of {num} is {factorial(num)}")


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
    else:
        result = 0
    return result


result = tri_recursion(6)
print(result)
