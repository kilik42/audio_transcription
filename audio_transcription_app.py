from turtle import title
import gradio as gr
from combine import merge_audio
# import speech_recognition as sr
import whisper

def transcribe_speech(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe( audio_file)

    return result["text"]

def main():
    # combine_audio()
    merge_audio()
    audio_input = gr.inputs.Audio(source="upload", type="filepath")
    output_text = gr.outputs.Textbox()

    iface = gr.Interface(fn=transcribe_speech, inputs=audio_input, outputs=output_text,title="Audio transcription", description="Transcribe audio files to text")

    iface.launch()

if __name__ == "__main__":
    main()
