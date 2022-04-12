def up_low(s):
    up = 0
    low = 0
    for x in s:
        if x.isupper():
           up+=1
        elif x.islower():
           low+=1
    print("No. of upper case characters : ",up)
    print("No. of lower case characters : ",low)         
up_low("Hello Mr. Rogers, how are you this fine Tuesday?")      