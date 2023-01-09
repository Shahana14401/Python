lst=[]
total=0
n=int(input("Enter the number of elements:"))
for i in range(n):
    val=input()
    lst.append(val)
for j in lst:
    total=total+j.count('a')
print("Occurence of a is:",total)
