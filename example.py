# Epoch Python Module Example Example File.
# Example on the epoch module features & functions.

# Import the epoch module:
import epoch

# -- TODAY() --

# The today() function returns today's date.

# Today as variable:
today = epoch.today()

# Print Today:
print ("Today's date & time:")
print (today)

# -- TIMEZONE() --

# The timezone() function returns a date with a diferent timezone.
# timezone() takes two(2) arguments:
#   - date = a date to be converted.
#   - tz = the timezone to convert to (ex. 'US/Pacific').

# Timezone_Set() as variable:
today_pst = epoch.timezone(today, 'US/Pacific')

# Print Timezone_Set():
print ("Today's date & time in Pacific time:")
print (today_pst)

# -- TIMEZONE_SET() --

# The timezone_set() function returns a date with a diferent timezone and new hour/minute/second values.
# timezone_set() takes five(5) arguments:
#   - date = a date to be converted.
#   - tz = the timezone to convert to (ex. 'US/Pacific').
#   - h = hour, changes the hour of the output.
#   - m = minute, changes the minute of the output.
#   - s = second, changes the second(s) of the output.

# Timezone_Set() as variable:
time = epoch.timezone_set(today, 'US/Pacific', 8, 0, 0)

# Print Timezone_Set():
print ("Todays' date at 8 o'clock Pacific time: ")
print (time)

# -- EPOCH_SEC() --

# The epoch_sec() function returns the seconds from the UNIX epoch (1970, 1, 1) to the inputed date.
# timezone_set() takes two(2) arguments:
#   - date = a date to be converted.
#   - tz = the timezone the date is in, (ex. 'US/Pacific').

# Epoch_Sec() as variable:
sec = epoch.epoch_sec(today_pst, 'US/Pacific')

# Print Epoch_Sec():
print ("Todays's date & time Pacific time as seconds since the epoch: ")
print (sec)
