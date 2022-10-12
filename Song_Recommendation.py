#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:15:54 2021

@author: rg
"""

import Camera
import pafy
import vlc
import os
import webbrowser


def song_recommendations():
    os.add_dll_directory(r"C:\Users\saikr\Desktop\Song-Recommendation-using-Facial-Emotion-Recognition-main\Song-Recommendation-using-Facial-Emotion-Recognition-main\VLC")
    emotion = Camera.snapshot()
    print("Your are " +emotion+ "\n")
    print(emotion + " Songs will play")
    if emotion == "Happy":
        url = "https://www.youtube.com/watch?v=LmyyE6slWrs"
        webbrowser.open(url)
    elif(emotion=="Angry"):
        url = "https://www.youtube.com/watch?v=FRkBZANnr6E"
        webbrowser.open(url)
    elif(emotion=="Sad"):
        url = "https://www.youtube.com/watch?v=yvnsgYQyGXo"
        webbrowser.open(url)
    elif(emotion=='Fear'):
        url = "https://www.youtube.com/watch?v=TAiHiDcdiYg"
        webbrowser.open(url)
    elif(emotion=='Suprise'):
        url = "https://www.youtube.com/watch?v=mqDPAI8Pt28"
        webbrowser.open(url)
    else:
        url = "https://www.youtube.com/watch?v=5vWESRaOMb8"
        webbrowser.open(url)

    
    
