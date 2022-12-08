#replace occurence of repeated string
word=input("Enter the string:")
char=word[0]
rep_string=word[0]+word[1:].replace(char,'$')
print(rep_string)
