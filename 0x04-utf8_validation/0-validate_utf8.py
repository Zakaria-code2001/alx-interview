#!/usr/bin/python3
"""
UTF-8 validation
"""


def validUTF8(data):
    """
    :type data: List[int]
    :rtype: bool
    """
    num_bytes = 0
    for number in data:
        byte = format(number, '08b')
        if num_bytes == 0:
            if byte.startswith('0'):
                continue
            elif byte.startswith('110'):
                num_bytes = 1
            elif byte.startswith('1110'):
                num_bytes = 2
            elif byte.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            if not byte.startswith('10'):
                return False
            num_bytes -= 1
    return num_bytes == 0
