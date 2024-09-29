
# Multimodal LLM for Mental Health Detection and Analysis

This project is designed to detect and analyze mental health conditions using a multimodal approach. The system processes audio samples (from interviews) and analyzes them using a language model (LLM) to derive mental health insights.

## Folder Structure

To organize the audio data, ensure the following folder structure is in place:

```
project_root/
│
├── audio_sample/                   # Audio clips from original interviews
│
├── inference.sh                     # Shell script to automate inference
└── auto_inference.py                # Python script for the inference pipeline
```

## Setup Instructions

### Step 1: Create Necessary Folders

In the root of your project directory, create the following folder structure:

`audio_sample/`: Add your audio clips:

### Step 2: Run the Inference

Once the folders are set up and the audio files are placed in the correct directories, you can initiate the analysis by running the following commands:

```bash
./inference.sh
python auto_inference.py
```

### Step 3: Verify Results

- The results from the multimodal analysis will be output by the inference script. You will get data in CSV named `inference_results.csv`.

## Scripts Overview

- **inference.sh**: This shell script helps automate the workflow for inference. Ensure all necessary dependencies and environment settings are configured before running.
- **auto_inference.py**: The main Python script that runs the multimodal analysis using the pre-trained LLM. Modify this script as necessary for your setup, particularly to adjust audio folder path.

## Notes

- You may need to adjust the configuration paths or filenames in `auto_inference.py` based on your dataset.
