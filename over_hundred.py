#check over 100
lst=[]
n=int(input("Enter the number of integers to be inserted on a list:"))
for i in range(n):
    elem=int(input())
    if(elem>=100):
        lst.append("over")
    else:
        lst.append(elem)
print(lst)
