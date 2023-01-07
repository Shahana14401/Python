n1=int(input("Enter the starting range:"))
n2=int(input("Enter the ending range:"))
flag=0
if(n1>=1000 and n2<10000):
    for i in range(n1,n2):
         for j in range(32,100):
                if((j*j)==i):
                    string=str(i)
                    if(int(string[0])%2==0 and int(string[1])%2==0 and int(string[2])%2==0 and int(string[3])%2==0):
                        print(i)
else:
    print(n1,"Enter a range of 4 digit number") 
