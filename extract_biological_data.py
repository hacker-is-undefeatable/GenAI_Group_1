import json
import os

file_path = """CORD_19_dataset_orginal_Copy/comm_use_subset/pdf_json/"""
write_path = """Data/Biological_Data.txt"""
dir_list = os.listdir(file_path)     # list of filename in path
num_of_files = len(dir_list)
print("Number of file: " + str(num_of_files))


def write_to_file(line, path):
    size = os.path.getsize(path)
    print(size)
    if size < 104857600:
        write_file = open(path, "a")
        try:
            write_file.write(line + "\n")
        except:
            UnicodeEncodeError
        write_file.close()
    else:
        exit(0)


for file in range(num_of_files):
    x = json.load(open(file_path + dir_list[file]))

    for i in range(len(x['abstract'])):
        line = x['abstract'][i]['text']
        write_to_file(line, write_path)

    for j in range(len(x['body_text'])):
        line = x['body_text'][j]['text']
        write_to_file(line, write_path)
