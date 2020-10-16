from io import StringIO

f = StringIO()
f.write('谷')
print(f.getvalue())
f.write('世宇')
print(f.getvalue())
f.close()
