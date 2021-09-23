import pytesseract
import PIL
from os import system
import re
system("tesseract -l")

class workout:
    reps = 0
    exercise_name = ""


def compile_text_to_workouts(text):
    workouts = []
    num = 0

   
    for word in text:
        new_workout = workout()
        if word.isdigit():
            new_workout.reps = word
            num+=1
        while num < len(text) and not text[num].isdigit() :
            new_workout.exercise_name +=  " " + str(text[num]) 
            num +=1
        if not new_workout.reps == 0 or not new_workout.exercise_name == "":
            workouts.append(new_workout)

    return workouts


####MAIN:###############################################################        

letters = (pytesseract.image_to_string(r'../GetFit/workout_routine1.png'))
print(letters)
sentence = re.findall(r'\w+', letters) ##turns letters into words and makes list
print(sentence)
compile_text_to_workouts(sentence) ###turns into actual workout routine
