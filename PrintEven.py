#print all the even nos in range 10

#logic with list comprehension
evenlist=[x for x in range(10) if x%2==0]
print(evenlist)

#Logic with for and if condition
evenlist =[]
for x in range(10):
 if x%2==0:
  evenlist.append(x)  
print(evenlist)
