 import csv

 with open ("empcsvread.csv",'w') as fp:
     w = csv.writer(fp)
     w.writerow(['empid','empdept','empcity'])
     w.writerows([
         [106,'IT','Pune'],
         [107,'pharma','nashik'],
         [108,'analyst','Hyderabad']
     ])
