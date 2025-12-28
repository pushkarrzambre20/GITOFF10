# import csv
# with open("empcsvread.csv") as fp:
#    r = csv.reader(fp)

# import csv
# with open("empcsvread.csv") as fp:
#    r = csv.reader(fp)
#   print(list(r))

# import csv
# with open("empcsvread.csv") as fp:
#    r = csv.reader(fp)
#    for line in r:
#        print(line)

# import csv
# with open("empcsvread.csv") as fp:
#    r = csv.reader(fp)
#    for line in r:
#     print(line[0],line[2])

# csv.reader mistakes
# – Expecting dictionary output (it returns a list)
# – Using column names like row['empid']
# – Forgetting CSV data is always read as strings
# – Assuming CSV has data types

# DictReader
# import csv
# with open('empcsvread.csv.','r') as file:
#        csvFile = csv.DictReader(file)
#        for lines in csvFile:
#             print(lines)

# import csv
# with open("empcsvread.csv") as fp:
#    r = csv.DictReader(fp)
#    for line in r:
#        print(line['name'],line['salary'])

# csv.DictReader mistakes
# – Using index like row[0] instead of key
# – Misspelling column names
# – Forgetting first row is treated as header
# – Expecting int or float values