import pytest
import itertools
import datetime


from time_tools import _generate_translate_options


def d(h, m):
    return datetime.datetime(2022, 1, 1, h, m)
        

def test_translate_time_compile():
    for hour, minute in itertools.product(range(24), range(60)):
        # generate all options
        list(_generate_translate_options(d(hour, minute)))


def test_translate_time_cases():
    for date, cases in (
        (d(12, 30), ['тридцать минут после полудня']),
        (d(3, 15), ['три часа пятнадцать минут']),
        (d(12, 0), ['ровно двенадцать часов']),
        (d(7, 59), ['без одной минут восемь']),
        (d(0, 0), ['ровно полночь']),
        (d(2, 1), ['два ноль одна']),
        (d(3, 45), ['без четверти четыре']),
        (d(6, 50), ['шесть пятьдесят']),
        (d(18, 50), ['без десяти минут девятнадцать'])
    ):
        options = [option.value for option in _generate_translate_options(date)]
        assert set(cases).issubset(set(options)), options

    