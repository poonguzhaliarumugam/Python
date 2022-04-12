def unique(mylist):
    myset=set(mylist)
    uniquelist=list(myset)
    print(uniquelist)
unique([1,1,1,1,2,2,3,3,3,3,4,5])  

#method2
def uniqlist(mylist):
    list2=[]
    for x in mylist:
        if x not in list2:
            list2.append(x)
    return(list2)
print(uniqlist([1,1,1,1,2,2,3,3,3,3,4,5]))            
