import pytesseract
import PIL
from os import system
import re
system("tesseract -l")


class workout:
      def __init__(self, reps, exercise_name):
        self.reps = reps    
        self.exercise_name = exercise_name


def compile_text_to_workouts(text):
    for word in text:
        if word.isDigit():
            reps = text[word]
            new_workout = workout(reps)
        else:
            print("")
            



