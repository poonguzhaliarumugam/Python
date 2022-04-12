listA=[1,2,4,4,1,4,2,6,2,9]
temp=[]
for i in listA:
    print("i: ",i)    
    if i in temp:
       del listA[i]
       print("listA: ",listA)
       continue
    else:
       temp.append(i)
       print("temp: ",temp)
print(temp)
