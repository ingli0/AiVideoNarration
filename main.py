from cut import extract_frames
from narration import generate_narration
from texttospeeachopenai import text_to_speech
from finalVideo import merge_audio_video

api_key = ""

def generate_narrated_video(video_path):
    
    image_folder = 'video'
    extract_frames(video_path, image_folder)
    generate_narration(api_key, image_folder)
    text_to_speech(api_key)
    merge_audio_video(video_path, 'output.mp3', 'final.mp4')

if __name__ == "__main__":
    video_path = 'your_video.mp4'  # Provide the path to your video
    generate_narrated_video(video_path)