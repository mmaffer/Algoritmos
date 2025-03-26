def factorial(n):
    if n == 0:
        return 1
    else:
       return n*factorial(n-1)

# example of its use
print (factorial(14))
print (factorial(8))
print (factorial(0))