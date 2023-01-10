def stringfun(string):
    if(string[-3:]=='ing'):
        print(string+'ly')
    else:
        print(string+'ing')
string=input("Enter the string:")
stringfun(string)
