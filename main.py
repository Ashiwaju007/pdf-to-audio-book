import pyttsx3
import PyPDF2

FILE_PATH = 'data.pdf'

engine = pyttsx3.init()
engine.setProperty('rate', 125)

with open(FILE_PATH, mode='rb') as f:

    reader = PyPDF2.PdfFileReader(f)

    page = reader.getPage(0)

    print(page.extractText())
    word = page.extractText()
    engine.say(word)
    engine.runAndWait()
    engine.stop()





