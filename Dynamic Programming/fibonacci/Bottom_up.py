# import time
from typing import List

def fibonacci(number: int, dp: List[int]) -> int:
    dp[0] = 0
    dp[1] = 1
    for i in range(2,number + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

if __name__ == "__main__":
    number: int = int(input("Enter a number : "))
    dp: List[int] = [-1] * (number + 1)
    
    result: int = fibonacci(number, dp)
    print(result)
