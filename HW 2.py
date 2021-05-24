what = input(' что делаем? (+, -):')
a = float(input('введи первое число:'))
b = float(input('введи второе число:'))

if what == '+':
    c = a + b
    print('Результат:' + str(c))

elif what == '-':
    c = a - b
    print('Результат:' + str(c))
# else:
#     print('chosen unknown operation')