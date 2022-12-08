#Create a list after removing even numbers
list1 = [10, 21, 4, 45, 66, 93]
print("The Original list is:",list1)
print("\nAfter removing even numbers:")
lst2=[]
for num in list1:
    if num % 2 != 0:
        lst2.append(num)
print(lst2)
