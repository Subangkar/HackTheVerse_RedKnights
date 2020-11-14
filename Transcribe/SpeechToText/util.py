from pydub import AudioSegment
import math
import speech_recognition as sr
r = sr.Recognizer()

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 15 * 1000
        t2 = to_min * 15 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 15)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            #print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


def speech_to_text_bangla(file_name):
    with sr.WavFile(file_name) as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

    try:
        list = r.recognize_google(audio,language="en-US")                  # generate a list of possible transcriptions
        #print("Possible transcriptions:")
        textOutput = ""
        for prediction in list:
            #print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
            #print(str(prediction))
            textOutput += str(prediction)
        #print(textOutput)
        with open("output1.txt","a",encoding="utf8") as outputFile:
            outputFile.write(textOutput + "\n")
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")