def myfunc(text):
   mystring=[]
   i=0
   for x in text:
      if i%2==0:
         #x=x.upper()
         mystring.append(x.upper())
      elif i%2!=0:
          #x=x.lower()  
          mystring.append(x.lower())
      i+=1    
   return ''.join(mystring)

print(myfunc('string test'))          
         
     