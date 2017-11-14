def factorial(n):
    # Complete this function
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
