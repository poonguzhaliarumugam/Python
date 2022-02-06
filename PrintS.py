#print only the words starting with s 
st='Print only the word that start with s in this sentence'
#for txt in st.split():
 #for val in txt:
  #if val[0] == 's':
   #print(txt)
   #continue

#Logic to print words starts with "S"
for txt in st.split():
    if txt[0] == 's':
        print(txt)
