import subprocess
import os

def extract_frames(video_path, output_folder):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

     
    subprocess.call(['ffmpeg', '-i', video_path, '-vf', 'fps=1', os.path.join(output_folder, 'frame%d.jpg')])

if __name__ == "__main__":
    video_file = 'dunk.mp4'  
    output_folder = 'video'   

    extract_frames(video_file, output_folder)
