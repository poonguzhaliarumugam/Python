def lesser_of_two_evens(x,y):
  if x%2==0 and y%2==0:
     return min(x,y)
  elif x%2!=0 or y%2!=0: 
     return max(x,y)

print(lesser_of_two_evens(10,27))        