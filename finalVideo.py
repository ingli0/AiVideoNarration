from moviepy.editor import VideoFileClip, AudioFileClip

 
video_path = 'lebrn.mp4'
audio_path = 'eleven.mp3'

def merge_audio_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()
    audio_clip.close()