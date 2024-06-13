import json
import os
from tqdm import tqdm

path = """CORD_19_dataset_orginal_Copy/noncomm_use_subset/noncomm_use_subset/pdf_json/"""          # edit this path
dir_list = os.listdir(path)     # list of filename in path
num_of_files = len(dir_list)
print("Number of file: " + str(num_of_files))
print(path + dir_list[0])

for file in tqdm(range(num_of_files), desc="Processing...", ascii=False, ncols=100):
    x = json.load(open(path + dir_list[file]))
    for i in range(len(x['body_text'])):
        for j in range(len(x['body_text'][i]['cite_spans'])):
            citation = x['body_text'][i]['cite_spans'][j]['text']
            citation2 = citation.replace('(', '')
            citation2 = citation.replace(')', '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace(citation, '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace(citation2, '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace("{", '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace("}", '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace("[", '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace("]", '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace("(", '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace(")", '')
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace(" . ", '')
        for k in range(len(x['body_text'][i]['ref_spans'])):
            x['body_text'][i]['text'] = x['body_text'][i]['text'].replace(x['body_text'][i]['ref_spans'][k]['text'], '')

    with open(path + dir_list[file], 'w') as f:
        json.dump(x, f)
