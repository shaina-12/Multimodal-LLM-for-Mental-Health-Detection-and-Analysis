
from inference_gradio import predict
import os
import csv

prompt = "Is the person in this audio depressed or not? Give me the answer in one word."

folder_path = 'audio_sample/Original_Trimmed_wav'
files = os.listdir(folder_path)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
csv_file_path = 'data.csv'
with open("og_trim.csv", mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['File name',"output"])
    for file_name in files:
        output = predict(folder_path+"/"+file_name,prompt)
        writer.writerow([file_name,output])

folder_path = 'audio_sample/Control_Trimmed_wav'
files = os.listdir(folder_path)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
with open("ctrl_trim.csv", mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['File name',"output"])
    for file_name in files:
        output = predict(folder_path+"/"+file_name,prompt)
        writer.writerow([file_name,output])

folder_path = 'audio_sample/Post_Interviews_Trimmed_wav'
files = os.listdir(folder_path)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
with open("pi_trim.csv", mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['File name',"output"])
    for file_name in files:
        output = predict(folder_path+"/"+file_name,prompt)
        writer.writerow([file_name,output])
