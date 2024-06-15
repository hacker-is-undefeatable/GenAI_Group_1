import json
import os

file_path = """65 Million Probably-Asked Questions/PAQ/PAQ_filtered.jsonl"""        # file to be processed
write_path = """65 Million Probably-Asked Questions/PAQ/Question.txt"""             # written file

count = 0
with open(file_path) as source:
    for line in source:
        count += 1
        line = line[14:line.find("\"", 14)]
        size = os.path.getsize(write_path)

        if size < 104857600:
            write_file = open(write_path, "a")
            write_file.write(line + "\n")
            write_file.close()
        else:
            exit(0)

        if count % 100000 == 0:
            print("Number of lines processed: " + str(count))
            print("File size: " + str(size))

