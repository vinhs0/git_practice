def printHello():
    print("Yel")

def countToN(n):
    for i in range(n):
        print(i)
    print("Merge Conflict")

def rebaseTest():
    print("Step 2")

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def mean_of_five(a, b, c, d, e):
    return (a + b + c + d + e) / 5

if __name__ == "__main__":
    countToN(4)