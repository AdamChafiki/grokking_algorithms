def countdown(i):
#   The base case 
  if i < 0:
    print("Done!")
    return
  print(i)
#   recursive case
  countdown(i-1)


# call stack 
def factoriel(n):
  if n==1 or n==0:
    return 1
  return n * factoriel(n-1) 


def fib(n):
    if n == 0:      # Base case 1
        return 0
    elif n == 1:    # Base case 2
        return 1
    return fib(n-1) + fib(n-2)



print(fib(3))