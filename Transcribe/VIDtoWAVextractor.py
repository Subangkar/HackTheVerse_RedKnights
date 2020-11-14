from moviepy.editor import *
audioclip = AudioFileClip("bizclass.mp4")
audioclip.write_audiofile("my_audio.wav")