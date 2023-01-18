import csv
with open('dep.csv') as files:
    data=csv.reader(files)
    for r in data:
        print(','.join(r))
