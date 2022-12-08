#fibnocci series
def fib(n):
    a,b=0,1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
        
n=int(input("Enter the number of terms:"))
print("Fibnocci series of first",n,"terms are:")
if(n==1):
    print(0)
elif(n==2):
    print(0)
    print(1)
else:
    fib(n)
