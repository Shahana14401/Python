import datetime
curr_date=datetime.datetime.now()
year=int(curr_date.year)
limit=int(input("Enter the last year to which leap year to be displayed:"))
for i in range(year,limit+1):
    if((i%100)==0):
        if((i%400)==0):
            print(i)
        else:
            continue
    elif((i%4)==0):
        print(i)
    else:
        continue
        
        
