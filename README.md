# quick-scripts

## strgen.py

### Help:
```
usage: strgen.py [-h] -l L [-n N] [-r]

optional arguments:
  -h, --help  show this help message and exit
  -l L        Length of desired string. Required argument.
  -n N        Number of desired strings. Defaults to 1.
  -r          Use random alphanumeric characters. Defaults to false.
```

### Examples
1. Generate a string of length 5
```
python strgen.py -l 5

aaaaa
```
2. Generate a random alphanumeric string of length 10
```
python strgen.py -r -l 10

gc0im7pmNy
```
3. Generate 5 random alphanumeric strings of length 7
```
python strgen.py -l 7 -n 5 -r

0v6HPVR
hestHHr
WoLFGs3
LVOtZkV
vDSwJqE
```

