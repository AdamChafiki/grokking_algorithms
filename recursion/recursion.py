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


def recursion(array:list):
    # base case
    if len(array) == 0:
        return 0
    #   recursive case
    return array[0] + sum(array[1:])
# sum
print(recursion([1,2,3,4,5]))


def count(array:list):
    if len(array) == 0:
        return 0
    return 1 + count(array[1:])
   

print(count([1,2,3,4,5]))


def maximum(array: list):
    if len(array) == 1:   
        return array[0]
    return max(array[0], maximum(array[1:]))

print(maximum([1, 2, 3, 4, 5]))  


def binary_search(arr, target):
    if len(arr) == 0:   
        return False
    mid = len(arr) // 2
    if arr[mid] == target:     
        return True
    elif arr[mid] > target:    
        return binary_search(arr[:mid], target)
    else:                      
        return binary_search(arr[mid+1:], target)

print(binary_search([1, 3, 5, 7, 9],7))