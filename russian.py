from num2words import num2words


def number_to_russian(number):
    return num2words(number, lang='ru')


def normilize_word(number: int, one, two, five):
    if 5 <= number <= 19:
        return five
    elif (number % 10) == 1:
        return one
    elif 2 <= (number % 10) <= 4:
        return two
    else:
        return five


def minute_in_nominative(minute: int, only_number=False):
    # Именительный падеж для минут
    
    if minute % 10 == 1:
        minute_word = (number_to_russian(minute) + ' ').replace('один ', 'одна')
    
    elif minute % 10 == 2:
        minute_word = (number_to_russian(minute) + ' ').replace('два ', 'две')
    else:
        minute_word = number_to_russian(minute)

    return minute_word.strip() + \
        (normilize_word(minute, ' минута', ' минуты', ' минут') if not only_number else '')

def minute_in_genitive(minute: int):
    # Родительный падеж для минут

    assert 1 <= minute <= 30

    numbers = [
        'одной', 'двух', 'трех', 'четырех', 'пяти',
        'шести', 'семи', 'восьми', 'девяти', 'десяти', 
        'одиннадцати', 'двенадцати', 'тринадцати', 'четырнадцати', 'пятнадцати', 
        'шестнадцати', 'семнадцати', 'восемнадцати', 'девятнадцати', 'двадцати', 
        'двадцати одной', 'двадцати двух', 'двадцати трех', 'двадцати четырех', 'двадцати десяти', 
        'двадцати шести', 'двадцати семи', 'двадцати восьми', 'двадцати девяти', 'тридцати'
    ]
    return numbers[minute - 1]


def hour_in_nominative(hour: int, only_number=False):
    # Именительный падеж для часа
    number_in_russian = number_to_russian(hour)
    if hour == 1:
        number_in_russian = 'час'
    if hour == 24 or hour == 0:
        return 'полночь'
    return number_in_russian + \
        (normilize_word(hour, ' час', ' часа', ' часов') if not only_number and hour != 1 else '')


def hour_in_genitive(hour: int):
    # Родительный падеж для часа

    assert 1 <= hour <= 12
    numbers = [
        'первого', 'второго', 'третьего', 'четвертого', 'пятого',
        'шестого', 'седьмого', 'восьмого', 'девятого', 'десятого', 
        'одиннадцатого', 'двенадцатого',
    ]
    
    return numbers[hour - 1]
