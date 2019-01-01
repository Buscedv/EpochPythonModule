# PyEpoch
Python module that can convert timezones, set time and calculate seconds since the UNIX epoch


# Installation

Download the epoch.py file and then import it into your python project.

```python3
import pyepoch
```

<br>

# Basic usage

How to use the functions in your code.

```python
# Gets todays date.
today = pyepoch.today()
```

<br>

# Documentation

Full documentation on all the functions:

## Today()

### The today() function
Returns todays date using datetime.datetime

### Ex.

```python
# Gets todays date.
today = pyepoch.today()
>>> 2018, 11, 8, 11, 32, 59, 744692
```

<br>

## Epoch_Sec()


### The epoch_sec() function
Returns seconds to a passed in date since the UNIX epoch (1970, 1 , 1)
The function takes two parameters:<br>
- A date: a datetime object
- A timezone: a timezone string, ex. 'US/Pacific'

### Ex.

```python
# Gets todays date.
today = pyepoch.today()
# Seconds since the epoch.
today = pyepoch.epoch_sec(today, 'US/Pacific')
>>> 2018, 11, 8, 11, 32, 59, 744692-08:00
```



## Timezone_Set()


### The timezone_set() function
Returns a passed in time in another timezone (also passed in) and sets the hour/minute/second in the passed in date.
The function takes five parameters:<br>
- A date: a datetime object to be converted.
- A timezone: a timezone string, ex. 'US/Pacific'
- Hour int
- Minute int
- Second int


### Ex.

```python
# Gets todays date.
today = pyepoch.today()
# Midnight pacific time today.
today = pyepoch.timezone(today, 'US/Pacific', 0, 0, 0)
>>> 2018-11-08 08:00:00-08:00
```

# Examples

You can download the 'example.py' file to see the functions in action.

# Contact
emial: <a href="mailto:edvard1807@gmail.com">edvard1807@gmail.com</a>
github: <a href="https://github.com/buscedv" traget="blank">@Buscedv</a>
<br><br>
Edvard Busck-Nielsen 2019
