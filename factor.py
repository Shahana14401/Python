def factor(n):
    print("Factor of %d are"%(n))
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
n=int(input("Enter the number:"))
factor(n)
