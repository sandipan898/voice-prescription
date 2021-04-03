from helper.pdf_op import  save_pdf
from helper.speech import speech_rec


def start_app():
    said = speech_rec()
    save_pdf(said)

if __name__ == '__main__':
    start_app()
