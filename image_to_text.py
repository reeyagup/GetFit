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
    workouts = []
    num = 0
    for word in text:
        if word.isdigit():
            new_workout = (word, text[num+1])
            workouts.append(new_workout)
            num+=1
    
    for x in workouts:
        print (x)

letters = (pytesseract.image_to_string(r'../GetFit/workout_routine.jpeg'))
text_words = re.findall(r'\w+', letters)
compile_text_to_workouts(text_words)
