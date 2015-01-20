# Fibonacci number

n=int(input("Please enter the position number:"))
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("\nThe Fibonacci number is", fib(n))
