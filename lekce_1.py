row = 1, 2, 3, 4
print(type(row))
print(row)
a = row[0]
print(*row, sep=': ', end='!\n')


def hello_n(name: str, n: int):
    for i in range(n):
        print('Hello,', name)


vas = 'Rey', 3
hello_n(*vas)


ass = range(0, 11, 10)
print(*ass)
for x in ass:
    print(x)

s = {'Moscov', 'Piter', 'Crazy'}
s.add('Riga')
print(s)
f = {'Moscov': 45666, 'Piter': 5444, 'Crazy': 25674}
f['Rostov'] = 31515
print(f)
for key in f:
    print((key, f[key]))


