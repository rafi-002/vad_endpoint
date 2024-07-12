import torch
import io
from silero_vad import (
    load_silero_vad,
    get_speech_timestamps,
    save_audio,
    read_audio,
    collect_chunks
)

model = load_silero_vad()

SAMPLING_RATE = 16000

def convert_audio(input_data: bytes, output_file: str) -> None:
    # Read the audio file in the .wav format
    audio_bytes = io.BytesIO(input_data)
    wav = read_audio(audio_bytes,SAMPLING_RATE)

    # Extract speech from the audio file
    speech_timestamps = get_speech_timestamps(wav, model, sampling_rate=SAMPLING_RATE)
    speech_wav = collect_chunks(speech_timestamps, wav)

    # Write the speech to the output file in the .wav format
    save_audio(output_file, speech_wav, sampling_rate=SAMPLING_RATE)
