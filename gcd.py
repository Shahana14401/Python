#gcd of two numbers
def gcd(n1,n2):
    a,b,r=n1,n2,-1
    while(r!=0):
        q=a//b
        r=a%b
        print(a,"=",b,"*",q,"+",r)
        a,b=b,r
    print("gcd of ",n1," and",n2," is:",a)
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
gcd(n1,n2)
