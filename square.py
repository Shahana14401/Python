#square of n numbers from given list
lst=[]
n=int(input("Enter the number of elements in list:"))
for i in range(n):
     elem=int(input())
     lst.append(elem)
print(lst)
print("Square of the elements in the above list are:")
for i in lst:
    print(i*i)
