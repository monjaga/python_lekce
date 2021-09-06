what = input('What (+, -)')

a = input('first number:')
b = input('second number:')
a = float(a)
b = float(b)

if what == '+':
    c = a + b
elif what == '-':
    c = a - b
else:
    c = 'ERROR'

print('result:' + str(c))


