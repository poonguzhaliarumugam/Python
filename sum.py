#sum of numbers to n
def sum(n):
 if n == 1:
  return 1
 else:
  return n + sum(n-1)
 
result = sum(4)
print(result)
