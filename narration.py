import base64
import requests
import json
import os

 
api_key = ""

 
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

 
def generate_image_paths(folder_path, num_images):
    return [os.path.join(folder_path, f"frame{i}.jpg") for i in range(11, 11 + num_images)]

 
image_folder = "video"

 
base64_images = [encode_image(image_path) for image_path in generate_image_paths(image_folder, 10)]

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
