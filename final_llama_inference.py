import os
import csv
from together import Together


output_file = "/media/nas_mount/shaina_mehta/baseline/ltu_new/ltu/src/ltu_as/inference/finetuned_final_eidc_inference_data.csv"
pre_eval = "/media/nas_mount/shaina_mehta/baseline/ltu_new/ltu/src/ltu_as/inference/finetuned_pre_eval.csv"

client = Together(api_key="e8e3b01f07efc427271e8708653e6e65a45e38a93b9aad0f5becd41e0df98e4b")

def get_together_response(transcript_data):
    prompt = [
        {
                "role": "user",
                "content": f"""
                You are a psychologist specializing in audio-based behavioral analysis. Your task is to determine whether a person is "Depressed" or "Not Depressed." You are provided with audio chunks from an interview, each described by its timestamp, transcript, and detailed audio features (such as tone, pitch, and other sound characteristics). Your role is to analyze these details and make an accurate assessment of the individual's mental state.

                Audio Details:
                {transcript_data}

                Based on these details, assess the individual's mental state and provide a final determination if the person is "Depressed" or "Not Depressed." Your answer must strictly be one of the following labels: "Depressed" or "Not Depressed.". Do not provide any explanation, analysis, or reasoning—output only the label: "Depressed" or "Not Depressed."
                """
        }
    ]

    response = client.chat.completions.create(
        model = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages = prompt,
        temperature = 0.1,
        repetition_penalty = 1,
        max_tokens = 50,
        stop = ["<|eot_id|>","<|eom_id|>"],
        stream = False
    )
    return response.choices[0].message.content


inference_data = {}
with open(pre_eval, mode='r') as file3:
    read_reader = csv.reader(file3)
    next(read_reader)
    for crow in read_reader:
        file_id = "_".join(crow[0].split("_")[:-1])
        if not file_id in inference_data:
            inference_data[file_id] = []
        inference_data[file_id].append({"response": crow[2],"transcript": crow[1]})

file_ids = []
for file_id, participant_data in inference_data.items():
    print(f"{file_id}: {len(participant_data)}")
    file_ids.append(file_id)
print(file_ids)
print(len(file_ids))
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

total_chuncks = len(inference_data)
progress = 0
start_time = 0
with open(output_file, mode='a', newline='') as file4:
    csv_writer = csv.writer(file4)
    for file_id, participant_data in inference_data.items():
        transcript_data = ""
        for participant_row in participant_data:
            transcript_data += f"""
            Timestamp: {start_time * 30}s - {(start_time+1) * 30}s
            Transcript: {participant_row["transcript"]}
            Audio Features: {participant_row["response"]}
            """
            start_time += 1
        progress += 1
        if file_id in inf_rows:
            print(f"--------------------------------------------------------------------------------")
            print(f"Skipping {file_id}, Progress: {progress}/{total_chuncks}")
            print(f"--------------------------------------------------------------------------------")
            continue
        response = get_together_response(transcript_data)
        csv_writer.writerow([file_id, transcript_data, response])
        print(f"--------------------------------------------------------------------------------")
        print(f"File ID: {file_id}")
        print(f"Response: {response}")
        print(f"Progress: {progress}/{total_chuncks}")
        print(f"--------------------------------------------------------------------------------")