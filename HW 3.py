print('Мальчик: Можно сигареты?')
print('Продавец: Тебе сколько лет?')
boy = int(input('Мальчик: мне '))

if boy < 18:
    print('Продавец: Эй малыш, тебе рано курить')
elif boy >= 18:
    print('Какую?')
    breakpoint()

if boy < 18:
    print('Мальчик: Мне больше 18!')
print('Продавец: А с какого года ты?')

boy1 = int(input('Мальчик: я с '))
year = 2021

if boy1:
    c = year - boy1
    print('Продавец: Тебе:' + str(c))
    if c < 18:
        print('Продавец: ты че? а нука покажи паспорт!')
    elif c >= 18:
        print('Продавец: все все верю')
