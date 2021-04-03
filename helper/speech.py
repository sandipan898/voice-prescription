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
    count = 0
    medicines = {}

    with sr.Microphone() as source:
        
        while(True):
            medicine_dict = {}
            count += 1

            print("Medicine-" + str(count) + " Information")            
        
            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)
            
            print("Medicine Name:")            
            speaker.say("Medicine name")
            
            recorded_audio = r.listen(source, timeout=6)
            print("Done")
        
            try:
                text = r.recognize_google(
                        recorded_audio, 
                        language="en-US"
                    )
                if((text.lower() == 'exit')):
                    break

                medicine_dict["Medicine Name"] = text
                print("Decoded Text : {}".format(text))   

            except Exception as e:
                print(e)


            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)
            
            print("Medicine Instruction:")  
            speaker.say("Medicine Instruction")

            recorded_audio = r.listen(source, timeout=6)
            print("Done")
        
            try:
                text = r.recognize_google(
                        recorded_audio, 
                        language="en-US"
                    )
                medicine_dict["Medicine Instruction"] = text
                print("Decoded Text : {}".format(text))   
                
            except Exception as e:
                print(e)

            medicines["Medicine No. " + str(count)] = medicine_dict
    
    return medicines


# print(speech_rec())
