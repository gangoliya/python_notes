def read_large(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

for line in read_large("big_file.txt"):
    print(line)


#   [2023-10-27 10:00:01] INFO: File 'example.tx' logged in.
#   [2023-10-27 10:00:05] WARN: Failed login attempt for 'Bob'.
#   [2023-10-27 10:00:10] INFO: Service 'payments' started.