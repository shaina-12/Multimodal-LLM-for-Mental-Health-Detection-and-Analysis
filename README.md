
# Multimodal LLM for Mental Health Detection and Analysis

This project is designed to detect and analyze mental health conditions using a multimodal approach. The system processes audio samples (from interviews and control groups) and analyzes them using a language model (LLM) to derive mental health insights.

## Folder Structure

To organize the audio data, ensure the following folder structure is in place:

```
project_root/
│
├── audio_sample/
│   ├── Original_Trimmed_wav/        # Audio clips from original interviews
│   ├── Control_Trimmed_wav/         # Audio clips from control group interviews
│   ├── Post_Interviews_Trimmed_wav/ # Audio clips from post-interviews
│
├── inference.sh                     # Shell script to automate inference
└── auto_inference.py                # Python script for the inference pipeline
```

## Setup Instructions

### Step 1: Create Necessary Folders

In the root of your project directory, create the following folder structure:

1. `audio_sample/`
   - Inside `audio_sample`, create these subfolders:
     - `Original_Trimmed_wav/`: Contains audio clips from original interviews.
     - `Control_Trimmed_wav/`: Contains audio clips from control group interviews.
     - `Post_Interviews_Trimmed_wav/`: Contains audio clips from post-interviews.

### Step 2: Add Audio Files

Add your audio clips into the corresponding folders:

- Place original interview audio files into `Original_Trimmed_wav/`.
- Place control group audio files into `Control_Trimmed_wav/`.
- Place post-interview audio files into `Post_Interviews_Trimmed_wav/`.

### Step 3: Run the Inference

Once the folders are set up and the audio files are placed in the correct directories, you can initiate the analysis by running the following commands:

```bash
./inference.sh
python auto_inference.py
```

### Step 4: Verify Results

- The results from the multimodal analysis will be output by the inference script. You will get data in CSV.

## Scripts Overview

- **inference.sh**: This shell script helps automate the workflow for inference. Ensure all necessary dependencies and environment settings are configured before running.
- **auto_inference.py**: The main Python script that runs the multimodal analysis using the pre-trained LLM. Modify this script as necessary for your setup, particularly to adjust audio folder path.

## Notes

- You may need to adjust the configuration paths or filenames in `auto_inference.py` based on your dataset.

## References:

[1] https://chatgpt.com/share/66f99972-c9bc-8007-a8bd-5415515e4267

[2] https://chatgpt.com/share/66f99989-4364-8007-b4e3-09eb67aa93ab
