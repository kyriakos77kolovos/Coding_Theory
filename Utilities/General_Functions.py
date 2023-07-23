from time import time
from base64 import b64decode, b64encode
from random import random, seed

from Utilities.Constants import PADDING


def _toBinary(char: int):
    return bin(char).replace("0b", "")


def toBinary(compressed_word: bytes):
    return "".join(_toBinary(ord_char).zfill(PADDING) for ord_char in tuple(compressed_word))


def _toByte(binary_word):
    return int(binary_word, 2)


def toBytes(binary_string):

    unpadded_binary_string_array = _unPadBinary(binary_string)
    binary_array = [_toByte(binary_word) for binary_word in unpadded_binary_string_array]

    return tuple(binary_array)


def _unPadBinary(binary_string):
    length_of_string = len(binary_string)
    unpadded_binary_string_array = []
    for i in range(0, length_of_string, PADDING):
        padded_word = binary_string[i: i + PADDING]
        index = padded_word.find('1')
        unpadded_word = padded_word[index:]

        unpadded_binary_string_array.append(unpadded_word)

    return unpadded_binary_string_array


def encodeBase64(binary_string: list):
    return b64encode("".join(list(map(str, binary_string))).encode())


def decodeBase64(encoded_data: bytes):
    return b64decode(encoded_data).decode()


def errorPercentage():
    while True:
        try:
            error_percentage = int(input("Select error percentage (0 or 100): "))
            break
        except Exception as e:
            print(e)

    if 0 < error_percentage <= 100:
        return 100

    return 0


def addNoise(binary_string, errors_percentage=0):
    seed(time())
    STOP_ERROR_FLAG, errors_added = False, 0
    for i in range(len(binary_string)):
        if not STOP_ERROR_FLAG and errors_added != errors_percentage:

            if random() < 0.91:
                continue

            if binary_string[i] == 0:
                binary_string[i] = 1
            else:
                binary_string[i] = 0

            errors_added += 100

            if errors_added == errors_percentage:
                STOP_ERROR_FLAG = True

    return binary_string
