from pydub import AudioSegment
import os
from together import Together
from inference_gradio import ltu_as_predict


ltu_prompt = "What is the emotion in this audio clip from perspective of mental health? Consider the Prosodic, Acoustic, Linguistic, temporal and Physiological markers in the audio while thinking. Give response in 1-2 lines. Is the person depressed or not. Be decisive."

client = Together(api_key="e8e3b01f07efc427271e8708653e6e65a45e38a93b9aad0f5becd41e0df98e4b")

def split_audio(audio_path, output_dir):
    audio = AudioSegment.from_file(audio_path)
    base_name, extension = os.path.splitext(os.path.basename(audio_path))
    chunk_duration = 30 * 1000
    total_duration = len(audio)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    saved_paths = []
    chunk_number = 1
    for start_time in range(0, total_duration, chunk_duration):
        end_time = min(start_time + chunk_duration, total_duration)
        chunk = audio[start_time:end_time]
        if len(chunk) < 1000:
            continue
        chunk_filename = f"{base_name}_{chunk_number}{extension}"
        chunk_path = os.path.join(output_dir, chunk_filename)
        chunk.export(chunk_path, format=extension[1:])
        saved_paths.append(chunk_path)
        
        print(f"Saved: {chunk_path}")
        chunk_number += 1
    
    return saved_paths

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

output_dir = "/media/nas_mount/shaina_mehta/baseline/ltu_new/ltu/src/ltu_as/live_chuncks"
def get_final_resp(audio_path):
    chuncks = split_audio(audio_path, output_dir)
    ltu_responses = []
    timestamp=0
    for chunck in chuncks:
        ltu_response, transcript = ltu_as_predict(chunck,ltu_prompt)
        print(ltu_response)
        print(transcript)
        start_time = timestamp*30
        timestamp += 1
        end_time = timestamp*30
        ltu_responses.append({"start_time": start_time, "end_time": end_time, "ltu_response": ltu_response, "transcript": transcript})

    transcript_data = ""
    for participant_row in ltu_responses:
        transcript_data += f"""
        Timestamp: {participant_row["start_time"]}s - {participant_row["end_time"]}s
        Transcript: {participant_row["transcript"]}
        Audio Features: {participant_row["ltu_response"]}
        """
    print(transcript_data)
    response = get_together_response(transcript_data)
    print(response)
    return response


