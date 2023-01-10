word=input("Enter any word:")
word_1=list(word)
print("Exchanged word is:")
temp=word_1[0]
word_1[0]=word_1[-1]
word_1[-1]=temp
print("".join(word_1))
