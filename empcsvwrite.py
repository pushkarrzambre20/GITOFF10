# import csv
#
# with open ("empcsvread.csv",'w') as fp:
#     w = csv.writer(fp)
#     w.writerow(['empid','empdept','empcity'])
#     w.writerows([
#         [106,'IT','Pune'],
#         [107,'pharma','nashik'],
#         [108,'analyst','Hyderabad']
#     ])

#with open ("empcsvread.csv",'w',newline='') as fp:

# import csv
#
# with open("empcsvread.csv", "w", newline="") as fp:
#     w = csv.writer(fp)
#     w.writerow(['empid', 'empdept', 'empcity'])
#     w.writerows([
#         [106, 'IT', 'Pune'],
#         [107, 'pharma', 'nashik'],
#         [108, 'analyst', 'Hyderabad']
#     ])

#DictWriter
#by using both writerow and writerows
# import csv
#
# with open("empcsvread.csv", "w") as fp:
#     fn = ['empid','empdept','empcity']
#     w = csv.DictWriter(fp,fieldnames=fn)
#     w.writeheader()
#     w.writerow({'empid':110,'empdept':'SE','empcity':'Mumbai'})
#     w.writerows([
#         {'empid': 106, 'empdept': 'IT', 'empcity': 'Pune'},
#         {'empid': 107, 'empdept': 'pharma', 'empcity': 'nashik'},
#         {'empid': 108, 'empdept': 'analyst', 'empcity': 'Hyderabad'}
#     ])

#by using writerows only
# import csv
#
# with open("empcsvread.csv", "w", newline="") as fp:
#     fn = ['empid', 'empdept', 'empcity']
#     w = csv.DictWriter(fp, fieldnames=fn)
#
#     w.writeheader()
#     w.writerows([
#         {'empid': 106, 'empdept': 'IT', 'empcity': 'Pune'},
#         {'empid': 107, 'empdept': 'pharma', 'empcity': 'nashik'},
#         {'empid': 108, 'empdept': 'analyst', 'empcity': 'Hyderabad'}
#     ])

# csv.DictWriter mistakes
# – Passing list instead of dictionary
# – Writing header manually after writeheader()
# – Wrong dictionary syntax (using set by mistake)
# – Missing keys (column becomes empty)

