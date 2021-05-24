en = {
    'apple': 'яблоко',
    'white': 'белый',
    'red': 'красный',
    'walk': 'ходить',
    'car': ['машина','авто']

}

ru = {
    'дата': 'date',
    'финик': 'date',
    'встреча': 'date',
    'свидания': 'date'

}


while True:
    lang = input('Выберите язык словаря: \n')
    if lang == 'ru':
        word = input('рус. - анг.: \n')
        try:
            print(ru[word])
        except KeyError:
            print('нет такого слова')
            action = input('новое слово? \n')
            if action == 'y':
                ru[word] = input(f'введите переовд к слову {word}')
    elif lang == 'en':
        word = input('анг. - рус.: \n')
        print(en[word])

    else:
        print('еще раз выберите язык словаря')
