#Check two list of integers
lst_1=[1,2,3,4,]
lst_2=[2,3,6,4,7]
if(len(lst_1)==len(lst_2)):
    print("The lists are of same length")
else:
    print("The lengths of two lists are not equal")
print("Sum of elements in lst_1=",sum(lst_1),"\nsum of elements in lst_2=",sum(lst_2))
if(sum(lst_1)==sum(lst_2)):
    print("The sum of elements are equal")
else:
    print("The sum of elements are not equal")
print("The repeating elements are:")
for i in lst_1:
    if i in lst_2:
        print(i)
