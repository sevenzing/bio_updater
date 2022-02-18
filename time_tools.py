from config import TIME_ZONE
from datetime import timedelta
from random import randrange, randint
import random
import dataclasses
import datetime
import pytz
import typing

from russian import hour_in_nominative, hour_in_genitive, minute_in_genitive, minute_in_nominative

@dataclasses.dataclass
class TranslateOption:
    """
    Possible option to represent datetime and weight to pick this datetime
    """
    value: str
    weight: float = dataclasses.field(default=1, compare=False)


T = TranslateOption

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def _generate_translate_options(date: datetime.datetime):
    """
    Generate possible options to represent datetime.
    """
    hour, minute = date.hour, date.minute

    hour_word = hour_in_nominative(hour)
    single_hour_word = hour_in_nominative(hour, only_number=True)
    minute_word = minute_in_nominative(minute)
    single_minute_word = minute_in_nominative(minute, only_number=True)

    if minute == 0:
        yield T(f"ровно {hour_word}", 20)

    elif minute == 30 and hour % 12 != 0:
        yield T(f"пол {hour_in_genitive(hour % 12 + 1)}", 20)

    elif hour == 0:
        if minute == 0:
            yield T("ровно полночь", 20)
        else:
            yield T(f"{minute_word} после полуночи", 10)
    
    elif hour == 12:
        if minute == 0:
            yield T("ровно полдень", 20)
        else:
            yield T(f"{minute_word} после полудня", 10)
    else:
        # 'Без' mode
        if minute >= 45:
            if minute == 45:
                yield T(f"без четверти {hour_in_nominative(hour + 1, only_number=True)}", 10)
            yield T(f"без {minute_in_genitive(60 - minute)} минут {hour_in_nominative(hour + 1, only_number=True)}", 5)
        
        if 1 <= minute <= 9:
            yield T(f"{single_hour_word} ноль {single_minute_word}", 6)

        if minute % 10 == 0:
            yield T(' '.join([single_hour_word, single_minute_word]), 8)

        yield T(' '.join([hour_word, minute_word]), 1)


def translate_time(date: datetime.datetime) -> str:
    options = list(_generate_translate_options(date))
    return random.choices(
        population=[o.value for o in options],
        weights=[o.weight for o in options],
        k=1,
    )[0]


def get_now() -> datetime.datetime:
    return  datetime.datetime.now(
        pytz.timezone(TIME_ZONE)
        )

def get_current_time_in_words():
    now = get_now()
    try:
        return translate_time(now)
    except:
        return now.strftime("%H %M")