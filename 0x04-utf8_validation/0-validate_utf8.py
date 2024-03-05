#!/usr/bin/python3
"""This module determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data):
    """This function determines if given data represents valid UTF-8 encoding
    Arguments:
        data: list of integers
    Returns:
        True if valid UTF-8 encoding, otherwise False
    """
    byte_num = 0

    first_mask = 1 << 7

    second_mask = 1 << 6
    for num in data:

        mask = 1 << 7
        if byte_num == 0:
            while mask & num:
                byte_num += 1
                mask = mask >> 1

            if byte_num == 0:
                continue

            if byte_num == 1 or byte_num > 4:
                return False
        else:
            if not (num & first_mask and not (num & second_mask)):
                return False
        byte_num -= 1
    return byte_num == 0
