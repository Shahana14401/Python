#Sum of items in list
lst=[]
sum=0
n=int(input("Enter the number of elements:"))
for i in range(n):
    elem=int(input())
    lst.append(elem)
print("List is:",lst)
for i in lst:
    sum=sum+i
print("Sum of all items in the list is:",sum)

