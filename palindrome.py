def palindrome(text):
    if (text[::-1]==text):
        return True
    else: return False    

print(palindrome('madam'))    