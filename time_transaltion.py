import datetime
from datetime import timedelta
from random import randrange, randint, choice
from russian import number_to_russian, hour_in_nominative, hour_in_genitive, minute_in_genitive, minute_in_nominative
from config import TIME_ZONE
import pytz

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def percent_chance(percent):
    return randint(0, 99) in range(percent)


def translate_time(date: datetime.datetime):
    hour, minute = date.hour, date.minute

    hour_word = hour_in_nominative(hour)
    single_hour_word = hour_in_nominative(hour, only_number=True)
    minute_word = minute_in_nominative(minute)
    single_minute_word = minute_in_nominative(minute, only_number=True)

    if minute == 0:
        return f"ровно {hour_in_nominative(hour)}"
    elif minute == 30 and hour % 12 != 0:
        return f"пол {hour_in_genitive(hour % 12)}"

    elif hour == 0:
        if minute == 0:
            return "ровно полуночь"
        else:
            return f"{minute_word} после полуночи"
    
    elif hour == 12:
        if minute == 0:
            return "ровно полудень"
        else:
            return f"{minute_word} после полудня"

    elif  minute >= 45 and percent_chance((45 * minute + 144 * hour)%100):
        # 'Без' mode
        if minute == 45:
            return f"без {choice(['пятнадцати', 'четверти'])} {hour_in_nominative(hour + 1, only_number=True)}"
        return f"без {minute_in_genitive(60 - minute)} минут {hour_in_nominative(hour + 1, only_number=True)}"
        
    else:
        if minute % 10 == 0 and percent_chance(80):
            return ' '.join([single_hour_word, single_minute_word])   
        else:
            return ' '.join([hour_word, minute_word]) 

def get_current_time_in_words():
    now = datetime.datetime.now(
        pytz.timezone(TIME_ZONE)
        )
    try:
        return translate_time(now)
    except:
        return now.strftime("%H %M")