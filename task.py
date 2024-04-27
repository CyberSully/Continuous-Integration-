
# Author - chauhand@oregonstate.edu
# SWE II - 3/4/2024

# helper function to convert string rep integreter into integret
# will iterate through each character in
# string and will convert digit to # value by finding
# .index in string '012345679' also multiply by 10 to shift digit to left"""
# check string using isdigit() returns none if non digit is found

def convert_integer(int_string, is_negative):
    if not int_string.isdigit():
        return None
    number = 0
    for c in int_string:
        number = number * 10 + '0123456789'.index(c)
    return -number if is_negative else number


# helper function to convert string rep hexadecimal into integreter
"""like convert int but processes hexadecimal digits, hence
0123456789abcdef and it will multiply number # by 16"""


def convert_hexadecimal(hex_string, is_negative):
    hex_string = hex_string.lower()
    if not all(c in '0123456789abcdef' for c in hex_string):
        return None
    number = 0
    for c in hex_string:
        number = number * 16 + '0123456789abcdef'.index(c)
    return -number if is_negative else number


# helper function to convert string rep float into float number
"""Uses split() to string into integer and decimal uses convert_int
helper to convert int and applies neg sign, ensures only 1 dec point"""


def convert_float_number(float_string, is_negative):
    if float_string.count('.') != 1:
        return None
    if not all(c in '0123456789.' for c in float_string):
        return None
    integer_part, decimal_part = float_string.split('.')
    number = convert_integer(integer_part, False) if integer_part else 0
    for i, c in enumerate(decimal_part):
        number += '0123456789'.index(c) * 10 ** -(i + 1)
    return -number if is_negative else number


"""Converts to numerical value, checks if number is negative, looks for 0x to
   represent hex, looks for decimal point for float,
   and if int convert_integer"""


def conv_num(num_str):
    if not isinstance(num_str, str) or num_str == '':
        return None

    is_negative = False
    if num_str[0] == '-':
        is_negative = True
        num_str = num_str[1:]

    if num_str.lower().startswith('0x'):
        return convert_hexadecimal(num_str[2:], is_negative)

    if '.' in num_str:
        return convert_float_number(num_str, is_negative)

    if num_str.isdigit():
        return convert_integer(num_str, is_negative)

    return None


# Author - Brett Sullivan
# SWE II - 3-4-2024

def conv_endian(num, endian='big'):
    """Converts an integer to hexadecimal with specified endian type."""
    if endian not in ['big', 'little']:
        return None

    if num < 0:
        negative = True
        # adds "-" for negative numbers on line 25 and
        # make sure variables keeps absolute value
        num = abs(num)
    else:
        negative = False

    result = []
    while num > 0:
        least_s_byte = num % 256  # Extract the least significant byte
        result.append(format(least_s_byte, '02X'))
        num //= 256       # Shift right by 8 bits

    if endian == 'big':
        result.reverse()

    if negative:
        return '-' + ' '.join(result)
    else:
        return ' '.join(result) if result else '00'


# Author: olsonr6@oregonstate.edu
# Date: 3/4/2024
def my_datetime(num_sec):
    """This function takes an integer value representing
    seconds since 01/01/1970, then converts
    it into a date, then returns the date as a string in "MM-DD-YYYY" format"""

    # function to check if given year is a leap year
    def is_leapyear(year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False

    # variables
    time_remaining = num_sec
    day = 1
    month = 1
    year = 1970

    # constants
    seconds_per_year = 31536000
    seconds_per_day = 86400

    # calculate year
    while ((is_leapyear(year) and time_remaining >= (
            seconds_per_year + seconds_per_day))
            or (not is_leapyear(year) and time_remaining >= seconds_per_year)):
        if is_leapyear(year):
            time_remaining -= (seconds_per_year + seconds_per_day)
        else:
            time_remaining -= seconds_per_year
        year += 1

    # calculate month
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year):
        days_per_month[1] = 29
    for i in range(0, 11):
        if time_remaining >= (days_per_month[i] * seconds_per_day):
            time_remaining -= (days_per_month[i] * seconds_per_day)
            month += 1
        else:
            break

    # calculate day
    day = time_remaining // seconds_per_day + 1

    # calculate result
    result = f"{month:02}-{day:02}-{year:04}"
    return result
