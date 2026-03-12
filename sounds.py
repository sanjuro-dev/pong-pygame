from pygame import mixer
from os import path

def init_sound():
    mixer.init()


def play_hit_sound():
    hit = mixer.Sound(path.dirname(__file__) + "/assets/hit.wav")
    hit.play()

def play_score_sound():
    score = mixer.Sound(path.dirname(__file__) + "/assets/score.wav")
    score.play()
