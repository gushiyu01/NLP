import json
import csv

json_file = open('./test.json', 'a+', encoding='utf-8')

with open('./20180721000000.export.CSV', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)
        print(row[1])
        d = {"s1": row[0], "s2": row[1]}
        print(json.dumps(d))
        json.dump(d, json_file)
        json_file.write('\n')


str1 = 'abc'
str2 = 'ABCdEfGH'
print(str1.capitalize())
print(str2.lower())
json_file.close()
