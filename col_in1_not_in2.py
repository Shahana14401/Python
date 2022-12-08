#colors in list 1 not in list 2
lst1=['red','green','blue','yellow','purple']
lst2=['blue','white','black','green']
for i in lst1:
    if(i not in lst2):
        print(i)
