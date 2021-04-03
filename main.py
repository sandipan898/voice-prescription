from helper.pdf_op import  save_pdf
from helper.speech import speech_rec


def start_app():
    medicines = speech_rec()
    print(medicines)
    save_pdf(medicines)

if __name__ == '__main__':
    start_app()
