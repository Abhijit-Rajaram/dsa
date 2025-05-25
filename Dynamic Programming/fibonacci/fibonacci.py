# import time
def fibonacci(n) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    number: int = int(input("Enter a number : "))
    # start_time = time.time()
    result: int = fibonacci(number)
    # end_time = time.time()
    # total_time = end_time - start_time
    print(result)
