def makes_twenty(x,y):
   if (x+y==20) or x==20 or y==20:
      return True 
   else:
      return False

print(makes_twenty(17,3)) 
print(makes_twenty(17,10))
print(makes_twenty(20,3))
print(makes_twenty(7,3))              