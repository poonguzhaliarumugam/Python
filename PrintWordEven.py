#print word if the no of letters in each word is even
st='print every word in this sentence that has an even number of letters'
wordlist=st.split()
for txt in wordlist:
 if len(txt)%2==0:
  print(txt+'- even!')
