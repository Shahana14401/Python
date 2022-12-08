#Swap char at position 1
a=input("Enter the first string:")
b=input("Enter the second string:")
a_temp=b[0:1]+a[1:]
b_temp=a[0:1]+b[1:]
a,b=a_temp,b_temp
print("After Swapping:",a,b)
