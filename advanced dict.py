from PyDictionary import PyDictionary
import pyttsx3
from pyttsx3 import engine


engine = pyttsx3.init()

def defination():
 word = str(input("Write the word you want know \n"))
 dict = PyDictionary()

 meaning = dict.meaning(word)
 n1 = meaning