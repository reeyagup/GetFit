import pytesseract
import PIL
from os import system
import re
system("tesseract -l")
letters = (pytesseract.image_to_string(r'../GetFit/workout_routine.jpeg'))

text_words = re.findall(r'\w+', letters)


