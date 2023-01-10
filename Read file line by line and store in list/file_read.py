f=open("lang.txt","r")
content=f.readlines()
c_list=[x.strip() for x in content]
print("The list of contents of file is:")
print(c_list)