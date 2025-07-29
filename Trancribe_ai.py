import os
from groq import Groq

# Step 1: Initialize Groq client with your actual API key
client = Groq(api_key='xxxxxyyyyyyyxxxxxxxxxx')  # ← Replace with your real API key

# Step 2: Provide the full path to your audio file using raw string to avoid escape issues
filename = r"C:\Users\klaks\OneDrive\Documents\DLK\batman\foxxx\Perfect - 320Kbps-(Mr-Jat.in).mp3"

# Step 3: Check if the file exists
if os.path.exists(filename):
    # Step 4: Open the file in binary read mode
    with open(filename, "rb") as file:
        # Step 5: Submit the audio for transcription
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3",
            prompt="Song lyrics transcription",  # Optional: improve context
            response_format="json",              # Structured output
            language="en",                       # English
            temperature=0.0                      # Deterministic output
        )

        # Step 6: Print the transcription result
        print("Transcription Result:")
        print(transcription.text)  # Ensure .text is valid for returned object

else:
    # Step 7: Handle missing file case
    print(f"Error: File not found at path -> {filename}")
