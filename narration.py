import base64
import requests
import json
import os

 
api_key = ""

image_folder = "video"
photo_extensions = ['.jpg']
photo_count = sum(len(files) for _, _, files in os.walk(image_folder) if any(file.endswith(ext) for ext in photo_extensions))

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

 
def generate_image_paths(folder_path, photo_count):
    return [os.path.join(folder_path, f"frame{i}.jpg") for i in range(1, 1 + photo_count)]

 


 
base64_images = [encode_image(image_path) for image_path in generate_image_paths(image_folder, photo_count)]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What are in these images? so write the response to be like you are a fan watching the game and discribe what happen in the images the difference after the previous image like a fan wathcing it real time  make the output short to need to read it in 30 seconds"
                }
            ] + [{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}} for base64_image in base64_images]
        }
    ],
    "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

with open("response.json", "w") as file:
    json.dump(response.json(), file)

print("Response JSON saved to response.json")
