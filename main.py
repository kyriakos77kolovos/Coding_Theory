from Compression_Algorithmss.Lempel_Ziv_78 import *

from Utilities.Constants import FILE_TO_COMPRESS, LOCATION_TO_SAVE, LOCATION_TO_UNCOMPRESS


with open(FILE_TO_COMPRESS, "rb") as file:
    file = file.read()

    compressed_file = compress(file)
    with open(LOCATION_TO_SAVE, "wb") as cf:
        cf.write(compressed_file)

    with open(LOCATION_TO_SAVE, "rb") as ucf:
        ucf = ucf.read()
        ucf = uncompress(ucf)

        with open(LOCATION_TO_UNCOMPRESS, "wb") as f:
            f.write(ucf)
            f.close()


def menu():
    print("1: Compress file")
    print("2: Uncompress file")
    print("3: Exit App")

    selection = input("Select an option:")
