try:
    input_file = open("datafile.txt", "r")

    input_file.close()
except FileNotFoundError:
    print("invalid file")