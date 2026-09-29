import random

RESPONSES =  [
    "It is certain",
    "Without a double",
    "Most likely",
    "Ask again later",
    "Can not predict",
    "The rain that fals",
 ]

def get_eight_ball_response():
    return random.choice(RESPONSES)