def fib(n, memo = {}):
    if (n in memo):
        return memo[n]
    elif (n <= 2):
        return 1
    else:
        return fib(n-1, memo) + fib(n-2, memo)

# Test the function
for i in range(100):
    print(i, fib(i))