import argparse
import string
import random

def get_char(use_random_chars):
    if (use_random_chars):
        char_set = string.digits + string.ascii_letters
        return random.choice(char_set)
    else:
        return 'a'
 
def get_string(length, use_random_chars):
    return ''.join(get_char(use_random_chars) for _ in xrange(length))

parser = argparse.ArgumentParser()
parser.add_argument('-l', type=int, help='Length of desired strings. Required argument.', required=True)
parser.add_argument('-n', type=int, help='Number of desired strings. Defaults to 1.', default=1)
parser.add_argument('-r', help='Use random alphanumeric characters. Defaults to false.', action='store_true')
args = parser.parse_args()

for _ in xrange(args.n):
    print(get_string(args.l, args.r))
