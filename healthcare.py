from pygame import init, mixer    
from datetime import datetime, time
from time import time


def musicinloop(file, stopper):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play(-1)
        while True:
            a = input()
            if a == stopper:
                mixer.music.stop()
                break

def log_now(msg):
        with open("mylogs.txt" , "a") as f:
            f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eye = time()
    init_exersise = time()

    watersecs =  2700
    eyessec =    1200
    exersise =   3600
    while True:
        if time( ) - init_water > watersecs:
            print("Drink Water reminder. Enter 'wd' if done ")
            musicinloop('waater.mp3' , 'wd')
            init_water = time()
            log_now ("drank water at")

        if time( ) - init_eye > eyessec:
            print("eye relexing reminder. Enter 'rd' if done ")
            musicinloop('eyee.mp3' , 'rd')
            init_eye = time()
            log_now ("eye relaxed at")

        if time( ) - init_exersise > exersise:
            print("Drink Water reminder. Enter 'ed' if done ")
            musicinloop('exerciise.mp3' , 'ed')
            init_exersise = time()
            log_now ("done exersise at")