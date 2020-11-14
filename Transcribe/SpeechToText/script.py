import os
from os import listdir
from os.path import isfile, join
from util import *

def main():
    folder = 'D:\\Projects\SpeechRecognition\Class_Recording'
    srcfile = 'audio_only.wav'
    split_wav = SplitWavAudioMubin(folder, srcfile)
    split_wav.multiple_split(min_per_split=1)

    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    for i in range(len(onlyfiles)-1):
        speech_to_text_bangla(folder + '\\' + str(i) + '_' + srcfile)


if __name__== "__main__":
  #main(int(sys.argv[1]))
  main()