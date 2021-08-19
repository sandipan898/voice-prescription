import sys
from helper.pdf_op import  save_pdf
from helper.speech import speech_rec_for_windows, speech_rec_for_linux


def start_app():
    if sys.platform.startswith('linux'):
        print("You are on Linux")
        medicines = speech_rec_for_linux()

    elif sys.platform.startswith('win32'):
        print("You are on Windows")
        medicines = speech_rec_for_windows()

    print(medicines)
    save_pdf(medicines)

if __name__ == '__main__':
    start_app()
