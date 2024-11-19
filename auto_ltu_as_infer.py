import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "3,2,0,1,5"
from inference_gradio import predict

import pickle
import csv

#pkl_file = "/media/nas_mount/shaina_mehta/baseline/ltu_new/ltu/src/ltu_as/inference/pre_eval.csv"
#output_file = "inference/finetuned_pre_eval.csv"
#audio_dir = "/media/nas_mount/shaina_mehta/osdvd/merged_audio"
#audio_dir = "/media/nas_mount/shaina_mehta/EDAIC/Test Set"

pkl_file = "/media/nas_mount/shaina_mehta/baseline/ltu_new/ltu/src/ltu_as/inference/pre_eval_osdvd_dataset.csv"
output_file = "inference/finetuned_pre_osdvd_eval.csv"
audio_dir = "/media/nas_mount/shaina_mehta/osdvd/merged_audio"


read_reader = csv.reader(open(pkl_file, mode='r'))
next(read_reader)
transcript_data = {}
total_chuncks = 0
inference_data = {}
for crow in read_reader:
    file_name = crow[0]
    name_without_extension = file_name.rsplit('.', 1)[0]
    split_parts = name_without_extension.split('_')
    file_id = '_'.join(split_parts[:-1])
    if file_id not in inference_data:
        inference_data[file_id] = []
    audio_path = f"{audio_dir}/{file_name}.wav" 
    inference_data[file_id].append({"file_name": crow[0],"transcript": crow[1], "audio_path": audio_path})
    total_chuncks += 1
    
inf_rows = []
if not os.path.exists(output_file):
    with open(output_file, mode='w', newline='') as file2:
        writer = csv.writer(file2)
        writer.writerow(['File Name', 'Content', 'Response'])
else:
    with open(output_file, mode='r') as file3:
        read_reader = csv.reader(file3)
        next(read_reader)
        for crow in read_reader:
            inf_rows.append(crow[0])
print(inf_rows)
prompt = """
What is the emotion in this audio clip from perspective of mental health? Consider the Prosodic, Acoustic, Linguistic, temporal and Physiological markers in the audio while thinking. Give response in 1-2 lines. Is the person depressed or not. Be decisive.
"""

progress = 0
for file_id, participant_data in inference_data.items():
    with open(output_file, mode='a', newline='') as file4:
        csv_writer = csv.writer(file4)
        for participant_row in participant_data:
            transcript = participant_row["transcript"]
            file_name = participant_row["file_name"]
            audio_path = participant_row["audio_path"]
            progress += 1

            if file_name in inf_rows:
                print(f"--------------------------------------------------------------------------------")
                print(f"Skipping {file_name}, Progress: {progress}/{total_chuncks}")
                print(f"--------------------------------------------------------------------------------")
                continue
            response = predict(audio_path,prompt)
            csv_writer.writerow([file_name, transcript, response])
            print(f"--------------------------------------------------------------------------------")
            print(f"Progress: {progress}/{total_chuncks}")
            print(f"--------------------------------------------------------------------------------")

