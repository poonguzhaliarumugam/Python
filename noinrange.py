#to find the no in range
def chk_ran(num,low,high):
    mylist=[x for x in range(low,high)]
    print(mylist)
    if num in mylist:
        return True
    else: return False

print(chk_ran(4,3,7))
#method2
def chk(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range of low amd high')
    else:
        print(f'{num} is not in range')    

chk(10,3,7)