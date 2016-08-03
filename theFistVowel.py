def theFirstVowel(st):
    vowel="aeiouAEIOU"
    count=0
    for i in st:
        if i in vowel:
            count+=1
        if count==1:
            return i
    if count==0:
        return "No Vowel!"
    
val = theFirstVowel("Pokemon-Go!")
print (val)
    
