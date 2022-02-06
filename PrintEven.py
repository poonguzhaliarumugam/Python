#print all the even nos in range 10
evenlist=[x for x in range(10) if x%2==0]
print(evenlist)
evenlist =[]
for x in range(10):
 if x%2==0:
  evenlist.append(x)  
print(evenlist)
