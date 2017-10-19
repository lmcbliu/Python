import csv, sys

lengths = {}

with open("C:/Algonquin/CST8333/DataSet/00010014-eng.csv", 'rt') as f:
    reader = csv.DictReader(f, delimiter=',') #pipe separated
    for index, row in enumerate(reader):
        if index == 0:
            for heading in row.keys():
                lengths[heading] = 0 #set the dict headings
        for column in row.keys():
            if (len(row[column]) > lengths[column]):
                lengths[column] = len(row[column]) #add length
    print (lengths)
    
    def returnIDs(IDfile):# extract the IDs
    IDs = set()
    with open(IDfile) as f:
        reader = csv.DictReader(f, fieldnames=['ID', 'other', 'fields'])
        for row in reader:
            IDs.add(row['ID'])
    return list(IDs)