
from inference_gradio import predict
import os
import csv

# prompt = """Based on the conversation in this audio, does the person show symptoms of depression? Provide a one-word answer: Yes if the person is depressed or No if the person is not depressed."""
prompt = "Is the person in this audio depressed or not? Give me the answer in one word."

folder_path = '/media/nas_mount/shaina_mehta/Daic-Woz-Extended/chunked_samples'
target_folder = "inference_data"
files = os.listdir(folder_path)

files_done_list = os.listdir(target_folder)
files_done=[]
for file_done_name in files_done_list:
    file_name_without_ext = os.path.splitext(file_done_name)[0]
    files_done.append(file_name_without_ext)
print(files_done)
for file in files:
    if file.startswith("dev_"):
        if file in files_done:
            continue
        with open(f"{target_folder}/{file}.csv", mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['File Name',"output"])
            csvs = os.listdir(f'{folder_path}/{file}') 
            for csvfile in csvs:
                file_path = f'{folder_path}/{file}/{csvfile}'
                output = predict(file_path,prompt)
                writer.writerow([csvfile,output])
                print(output)