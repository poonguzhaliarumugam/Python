import string
#print(string.ascii_lowercase)
def pangram(text,alphabet=string.ascii_lowercase):
    set1=set((text.lower()).replace(" ",""))#converting to a set to eliminate duplicates
    mylist=list(set1)
    mylist.sort()
    newtext="".join(mylist)
    if newtext==alphabet:
        return True
    else: return False    
    
print(pangram("The quick brown fox jumps over the lazy dog"))
#print(pangram('hello'))