def factorial(n):
    if n==0:
        return 1
    else :
      fact=n*factorial(n-1)
      return fact
print(factorial(5))    