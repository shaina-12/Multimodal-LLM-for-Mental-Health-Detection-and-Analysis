import os
import csv

pkl_file = "/media/nas_mount/shaina_mehta/osdvd/train_test_split.csv"
output_file = "pre_eval_other_dataset.csv"
output_file_2 = "pre_eval_osdvd_dataset.csv"

read_reader = csv.reader(open(pkl_file, mode='r'))
next(read_reader)
inference_data = []
for crow in read_reader:
    file_name = crow[0]
    if crow[2] == "test":
        inference_data.append(file_name)
print(inference_data)


read_reader_2 = csv.reader(open(output_file, mode='r'))
next(read_reader_2)

with open(output_file_2, mode='w', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerow(['File Name', 'Content', 'Response'])
    for crow2 in read_reader_2:
        if crow2[0] in inference_data:
            writer.writerow([crow2[0], crow2[1], crow2[2]])



