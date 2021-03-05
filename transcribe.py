import math
from re import A, L
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

current_dir = os.getcwd()
filename = 'skepticast2021-02-27'

MP3_SOURCE = os.path.join(current_dir, 'source', filename + '.mp3')
AUDIO_FILE = os.path.join(current_dir, 'source', filename + '.wav')


class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '/' + filename

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


# def load_chunks(filename):
#     long_audio = AudioSegment.from_mp3(filename)
#     audio_chunks = split_on_silence(
#         long_audio, min_silence_len=1800,
#         silence_thresh=-17
#     )
#     return audio_chunks


# for audio_chunk in load_chunks('./source/skepticast2021-02-27.mp3'):
#     audio_chunk.export("temp", format="wav")
#     with sr.AudioFile("temp") as source:
#         audio = sr.Recognizer().listen(source)
#         try:
#             text = sr.Recognizer().recognize_google(audio)
#             print("Chunk : {}".format(text))
#         except Exception as ex:
#             print("Error occured")
#             print(ex)

# print("++++++")


# split_wav = SplitWavAudioMubin(os.path.join(
#     current_dir, 'source'), 'skepticast2021-02-27.wav')
# split_wav.multiple_split(min_per_split=2)

# # convert mp3 file to wav
# sound = AudioSegment.from_mp3(MP3_SOURCE)
# sound - sound[6000:12000]
# sound.export(AUDIO_FILE, format='wav')


# transcribe audio file
# use the audio file as the audio source
f = os.path.join(current_dir, 'source', '0_skepticast2021-02-27.wav')
r = sr.Recognizer()
with sr.AudioFile(f) as source:
    audio = r.record(source)  # read the entire audio file

    print("Transcription: " + r.recognize_google(audio))
