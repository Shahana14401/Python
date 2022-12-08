#display pyramid with no of steps accepted from user
#eg:n=4
"""
1
2 4
3 6 9
4 8 12 16
"""

n=int(input("Enter the number of steps:"))
for i in range(1,n+1):
    print("\n")
    for j in range(1,i+1):
        print(i*j,end=' ')
