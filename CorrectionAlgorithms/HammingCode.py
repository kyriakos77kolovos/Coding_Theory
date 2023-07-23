from functools import reduce


def _calcRedundantBits(data_length):
    # Use the formula 2 ^ r >= m + r + 1
    # to calculate the no of redundant bits.
    # Iterate over 0 .. m and return the value
    # that satisfies the equation

    for i in range(data_length):
        if 2 ** i >= data_length + i + 1:
            return i


def _posRedundantBits(data):
    data_length = len(data)
    number_of_parity_bits = _calcRedundantBits(data_length)

    data = data[::-1]
    # Redundancy bits are placed at the positions
    # which correspond to the power of 2.
    j, k = 0, 0
    hamming_data_res = ''

    # If position is power of 2 then insert '0'
    # Else append the data
    for i in range(1, data_length + number_of_parity_bits + 1):
        if i == 2 ** j:
            hamming_data_res += '0'
            j += 1
            continue

        hamming_data_res += data[k]
        k += 1

    return hamming_data_res


def _calcParityBits(data):
    new_data = [0]
    data = list(map(int, data))
    parity_bit = 0

    # Going through the list to find the parity bits positions
    for bit in range(len(data)):
        parity = 2 ** parity_bit

        # checking if the position of parity bit is the current index + 1
        if parity == bit + 1:
            i = parity - 1
            tmp = []

            # Finding all word bits for each parity bit
            while i < len(data):
                tmp.extend(data[i:i + parity])
                i += 2 * parity

            # On the parity positions - 1 calculating their value using XOR ( ^= )
            for j in range(1, len(tmp)):
                data[parity - 1] ^= tmp[j]

            parity_bit += 1

    new_data.extend(data)
    new_data[0] = list(map(str, new_data)).count('1') % 2   # Calculating root parity

    return new_data


def detectAndFixError(data: list):
    error_index = reduce(lambda x, y: x ^ y, [index for index, bit in enumerate(data) if bit])

    if data[error_index] == 1:
        data[error_index] = 0
    else:
        data[error_index] = 1

    return "".join(list(map(str, data))), error_index


def removeParities(data):
    data = data[1:]  # Removing root parity

    parity_bit, original_data = 0, []

    for i in range(len(data)):
        parity = 2 ** parity_bit

        if i + 1 == parity:
            parity_bit += 1
            continue

        original_data.append(data[i])

    return "".join(list(map(str, original_data[::-1])))


def posAndCalcParities(data):
    parity_data = _posRedundantBits(data)
    hamming_data = _calcParityBits(parity_data)

    return hamming_data
