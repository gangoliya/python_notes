def read_large(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

for line in read_large("big_file.txt"):
    print(line)