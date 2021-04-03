import speech_recognition as sr
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import espeak


espeak.init()
speaker = espeak.Espeak()
# speaker.rate = 300
# speaker.say("Faster hello world")

def load_chunks(filename):
    long_audio = AudioSegment.from_mp3(filename)
    audio_chunks = split_on_silence(
        long_audio, min_silence_len=1800,
        silence_thresh=-17
    )
    return audio_chunks

def speech_rec():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting noise ")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = r.listen(source, timeout=6)
        print("Done recording")       # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            # print("Text: "+r.recognize_google(audio_text, language = 'bn-IN'))
            # print("Text: "+r.recognize_google(audio_text))
            text = r.recognize_google(
                    recorded_audio, 
                    language="en-US"
                )
            print("Decoded Text : {}".format(text))   
            speaker.say(text)
            return text

        except Exception as e:
                print(e)
                return "Sorry, I did not get that"

# speech_rec()