# from pygdelt.gdeltv2 import Events, GKG, Mentions
# from datetime import datetime
#
# ev = Events()
# query = ev.query(datetime(2020, 7, 21))
# print(query)

# mtn = Mentions()
# mtn.query(datetime(2018, 7, 21))
#
# gkg = GKG()
# gkg.query(datetime(2018, 7, 21))

import csv


with open('C:\\Users\\dell\\Desktop\\20201020.export.CSV\\20201020.export.CSV', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    flag = 223
    for row in reader:
        flag = flag - 1
        print(row)
        print(len(row))
        if flag == 0:
            break
