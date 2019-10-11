# A media access control address (MAC address) is a unique identifier assigned to
# network interfaces for communications on the physical network segment.
#
# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly
# form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by
# hyphens (e.g. 01-23-45-67-89-AB).
#
# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.
#
# Example
#
# For inputString = "00-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = true;
# For inputString = "Z1-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = false;
# For inputString = "not a MAC-48 address", the output should be
# isMAC48Address(inputString) = false.
import re


def isMAC48Address(inputString):

    # It accepts 12 hex digits with either : or - or nothing as separators between pairs
    # (but the separator must be uniform... either all separators are : or are all - or there is no separator).
    #
    # This is the explanation:
    #
    # * [0-9a-f] means an hexadecimal digit
    # * {2} means that we want two of them
    # * [-:]? means either a dash or a colon but optional. Note that the dash as first char doesn't
    #   mean a range but only means itself. This subexpression is enclosed in parenthesis so it can
    #   be reused later as a back reference.
    # * [0-9a-f]{2} is another pair of hexadecimal digits
    # * \\1 this means that we want to match the same expression that we matched before as separator.
    #   This is what guarantees uniformity. Note that the regexp syntax is \1 but I'm using a regular
    #   string so backslash must be escaped by doubling it.
    # * [0-9a-f]{2} another pair of hex digits
    # * {4} the previous parenthesized block must be repeated exactly 4 times,
    #   giving a total of 6 pairs of digits: <pair> <sep> <pair> ( <same-sep> <pair> ) * 4
    # * $ The string must end right after them
    # * Note that in Python re.match only checks starting at the start of the string and
    #   therefore a ^ at the beginning is not needed.

    # if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", inputString.lower()):
    #     return True
    # else:
    #     return False

    # Even shorter
    return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s))


print(isMAC48Address("00-1B-63-84-45-E6"))
print(isMAC48Address("Z1-1B-63-84-45-E6"))
print(isMAC48Address("not a MAC-48 address"))
