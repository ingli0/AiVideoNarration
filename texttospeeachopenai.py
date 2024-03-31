from openai import OpenAI
import json

api_key = ""

def text_to_speech(api_key):
    client = OpenAI(api_key=api_key)

    
    with open('response.json', 'r') as file:
        data = json.load(file)
    
    content = data["choices"][0]["message"]["content"]

    audio = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=content,
    )

    audio.stream_to_file("output.mp3")