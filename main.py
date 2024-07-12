import filetype
from fastapi import FastAPI, File, UploadFile, HTTPException
from audio_converter import convert_audio


app = FastAPI()

@app.post("/convert_audio")
async def convert_audio_endpoint(file: UploadFile = File(...)):
    # Check the input data format
    input_data = await file.read()

    # Convert the audio file
    output_file = "output.wav"
    convert_audio(input_data, output_file)

    # Return a message indicating that the conversion was successful
    return {"message": f"Conversion successful. Output file: {output_file}"}
