from logging import root
import speech_recognition as sr
from tkinter import *
import pyttsx3
engine=pyttsx3.init()
voiceId="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voiceId)
engine. setProperty("rate", 135)


