# EpochPythonModule
Python module that can convert timezones, set time and calculate seconds since the UNIX epoch


# Installation

Download the epoch.py file and then import it into your python project.

```python3
import epoch
```

<br>

# Basic usage

How to use the functions in your code.

```python
# Gets todays date.
today = epoch.today()
```

<br>

# Documentation

Full documentation of all the functions:

## Today()
<br>
### The today() function
Returns todays date using datetime.datetime

### Ex.

```python
# Gets todays date.
today = epoch.today()
>>> 2018, 11, 8, 11, 32, 59, 744692
```

<br>

## Epoch_Sec()
<br>
### The epoch_sec() function
Returns seconds to a passed in date since the UNIX epoch (1970, 1 , 1)
The function takes two parameters:<br>
- A date: a datetime object
- A timezone: a timezone string, ex. 'US/Pacific'
<br>
### Ex.

```python
# Gets todays date.
today = epoch.today()
# Seconds since the epoch.
today = epoch.epoch_sec(today, 'US/Pacific')
>>> 
```

<br>

## Timezone_Set()
<br>
### The timezone_set() function
Returns a passed in time in another timezone (also passed in) and sets the hour/minute/second in the passed in date.
The function takes five parameters:<br>
- A date: a datetime object to be converted.
- A timezone: a timezone string, ex. 'US/Pacific'
- Hour int
- Minute int
- Second int
<br>
### Ex.

```python
# Gets todays date.
today = epoch.today()
# Midnight pacific time today.
today = epoch.timezone(today, 'US/Pacific', 0, 0, 0)
>>> 2018-11-08 08:00:00-08:00
```

<br>
# Contact
emial: <a href="mailto:edvard1807@gmail.com">edvard1807@gmail.com</a>
github: <a href="https://github.com/buscedv" traget="blank">@Buscedv</a>
<br><br>
Edvard Busck-Nielsen 2018
