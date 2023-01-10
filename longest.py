lst=[]
n=int(input("Enter the number of words:"))
for i in range(n):
    s=input()
    lst.append(s)
k=0
for j in lst:
    if(k<len(j)):
        lrg=j
    k=len(j)
print("Longest word is:",lrg)
print("Length is:",len(lrg))
