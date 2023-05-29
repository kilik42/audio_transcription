# combine two audio files into one using python moviepy
from typing import final
from pydub import AudioSegment
from turtle import title
import gradio as gr
from moviepy.editor import concatenate_audioclips, AudioFileClip
import os


# Directory path containing audio files
# directory = '/path/to/audio/files'
def merge_audio(directory, output_path):
    # Initialize an empty AudioSegment object to store the merged audio
    merged_audio = AudioSegment.empty()

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.mp3') or filename.endswith('.wav'):
            file_path = os.path.join(directory, filename)

            # Load the audio file
            audio = AudioSegment.from_file(file_path)

            # Append the audio to the merged_audio object
            merged_audio += audio

    # Export the merged audio to a file
    merged_audio.export(output_path, format='wav')
    return "Merged audio file created successfully."

input_directory = gr.inputs.Textbox(label="Input Directory")
output_path = gr.inputs.Textbox(label="Output File Path")

output_text = gr.outputs.Textbox()

title = "Audio File Merger"
description = "Merge multiple audio files into a single audio file and save it to disk. Then it will be transcribed"

examples = [["/path/to/audio/files", "/path/to/output/merged_audio.wav"]]

gr.Interface(fn=merge_audio, inputs=[input_directory, output_path], outputs=output_text, title=title, description=description, examples=examples).launch()