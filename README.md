AI Video Narration Code using OpenAI Api

This code repository provides a comprehensive solution for generating narrations for videos using artificial intelligence. The process involves segmenting the input video into frames, analyzing each frame to generate text narration using OpenAI's Computer Vision API, converting the generated text into speech using OpenAI's Text-to-Speech API, and finally merging the narration with the original video to produce a narrated version.

Overview:
The code consists of three main Python scripts: cut.py, narration.py,texttospeeachopenai.py , and finalvideo.py. Each serves a specific purpose in the process of creating narrated videos.

# Cut.py:
This script is responsible for segmenting the input video into frames.
Each frame is extracted at regular intervals (e.g., one frame per second) and saved as an image.
These images are stored in a folder named "video."

## narration.py:
Utilizes OpenAI's Computer Vision API to analyze the images extracted from the video.
Generates textual narrations based on the content of the images.
The generated text is stored further for speech synthesis.

### texttospeeachopenai.py
Utilizes OpenAI's Text-to-Speech API to convert the generated text narrations into speech.
Outputs the synthesized speech as an MP3 file named "output.mp3." 

#### finalvideo.py:
Mutes the original video.
Incorporates the synthesized narration (output.mp3) into the muted video.
Produces the final narrated video.

##### TEST
using this video :https://youtu.be/G7oPeKhTfy0

the result is : https://youtu.be/cRkxl7qBr3I
