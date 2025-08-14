# Replace a specific word in a large text file using seek() & tell()

old_word = "fail"
new_word = "pass"  # must be same length as old_word

with open("python_teaching/assignments/log.txt", "r+") as file:
    while True:
        pos = file.tell()
        line = file.readline()
        if not line:
            break
        if old_word in line:
            updated_line = line.replace(old_word, new_word)
            file.seek(pos)
            file.write(updated_line)