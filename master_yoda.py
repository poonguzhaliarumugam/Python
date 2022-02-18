#method1
def master_yoda(text):
  i=0
  templist=[]
  mylist=text.split()
  listlen=len(mylist) 
  while(i<listlen):
    i+=1
    templist.append(mylist[listlen-i])
    
  return " ".join(templist)

print (master_yoda('We are ready'))

#Method2
def master_yoda2(text):
   wordlist=text.split()
   wordlist=wordlist[::-1]
   return " ".join(wordlist)

print(master_yoda2("We are ready"))   


       