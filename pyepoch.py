# PyEpoch Module
# Python module that can convert timezones, set time and calculate seconds since the UNIX epoch
# 1.0
# Edvard Busck-Nielsen 2018
# GNU GPL v. 3.0

# !! Requres both datetime && pytz installed and Python 3 !!

def epoch_sec(date, tz): # Gets seconds scince the UNIX Epoch takes a date and a timezone.
    import pytz
    import  datetime
    pst = pytz.timezone(tz)
    epoch = pst.localize(datetime.datetime(1970,1,1))
    # Calculates epoch seconds.
    delta_time = (date - epoch).total_seconds()
    # Returns the seconds.
    return delta_time

def timezone(date, tz): # Converts timezone takes a date and a timezone.
    import pytz
    import  datetime
    pst = pytz.timezone(tz)
    i = pst.localize(date)
    return i
def timezone_set(date, tz, h, m, s): # Converts timezone & sets time to get ex. Midnight Pacific Time.
    import pytz
    import  datetime
    pst = pytz.timezone(tz)
    i = pst.localize(datetime.datetime(date.year, date.month, date.day, h, m, s))
    return i
def today(): # Returns todays date
    import pytz
    import datetime
    return datetime.datetime.now()
