from Compression_Algorithmss.Lempel_Ziv_78 import compress, uncompress

from Utilities.Constants import PADDING, LOCATION_TO_SAVE, LOCATION_TO_UNCOMPRESS
from CorrectionAlgorithms.HammingCode import posAndCalcParities, detectAndFixError, removeParities
from Utilities.General_Functions import toBinary, encodeBase64, decodeBase64, errorPercentage, addNoise, toBytes

WORD = "Hello my name is Constantinos."


def test_compress():
    # Compress word
    print("---Compressing---")
    print("Compressing msg: {}".format(WORD))
    compressed_word = compress(bytes(WORD.zfill(PADDING).encode()))

    # Converting decimal representation to binary and padding binary to target length
    print("Converting to binary and creating parities...")
    compressed_binary_string = toBinary(compressed_word)
    parity_numbers = posAndCalcParities(compressed_binary_string)

    # Adding noise
    print("Adding noise...")
    error_percentage = errorPercentage()
    noisy_binary_string = addNoise(parity_numbers, error_percentage)
    print("Noise added with value: {}%".format(error_percentage))
    encoded_string = encodeBase64(noisy_binary_string)
    print("Converting to base64...")

    with open(LOCATION_TO_SAVE, "wb") as f:
        f.write(encoded_string)
        f.close()

    print("Converting completed\n")


def test_decompress():
    print("---Decompressing---")
    with open(LOCATION_TO_SAVE, "rb") as f:
        print("Loading file...")
        decoded_string = decodeBase64(f.read())
        decoded_string = list(map(int, decoded_string))
        print("Detecting and fixing error...")
        fixed_decoded_string, errors = detectAndFixError(decoded_string)
        if errors > 0:
            print("Fixed 1 error")
        else:
            print("No errors found")
        decoded_string = removeParities(fixed_decoded_string)
        bytes_chars = toBytes(decoded_string)
        print("Decompressing file...")
        original_data = uncompress(bytes_chars)
        print("Original msg: {}".format(original_data.decode()))


if __name__ == "__main__":
    test_compress()
    test_decompress()
