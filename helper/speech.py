import speech_recognition as sr
# from pydub import AudioSegment
# from pydub.silence import split_on_silence
import espeak

espeak.init()
speaker = espeak.Espeak()


def save_information():
    pass


def speech_rec():
    r = sr.Recognizer()
    text = ""
    count = 1
    medicines = {}

    with sr.Microphone() as source:
        
        while(not (text.lower() == 'exit')):
            medicine_dict = {}
            print("Medicine-%d Information", count)            
            count += 1
        
            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Medicine Name:")            
            recorded_audio = r.listen(source, timeout=6)
            print("Done")
        
            try:
                speaker.say("Medicine name")
                text_name = r.recognize_google(
                        recorded_audio, 
                        language="en-US"
                    )
                medicine_dict["Medicine Name"] = text_name
                print("Decoded Text : {}".format(text))   
                
                # speaker.say(text)
                # return text

            except Exception as e:
                print(e)
                # return "Sorry, I did not get that"



            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Medicine Instruction:")            
            recorded_audio = r.listen(source, timeout=6)
            print("Done")
        
            try:
                speaker.say("Medicine Instruction")
                text_instruction = r.recognize_google(
                        recorded_audio, 
                        language="en-US"
                    )
                medicine_dict["Medicine Instruction"] = text_instruction
                print("Decoded Text : {}".format(text_instruction))   
                
                # speaker.say(text)
                # return text

            except Exception as e:
                print(e)
                # return "Sorry, I did not get that"

            medicines["medicine" + str(count)] = medicine_dict
    
    return medicines


print(speech_rec())
