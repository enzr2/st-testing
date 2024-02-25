text = """
import string #import these things for the code to work
import random
import webbrowser

from .food_list import food
from .song_lists import happysong, sadsong, angrysong, fearsong
from .word_lists import happy_list, sad_list, angry_list, fear_list

#jake word detector
def coursework(text):
    output = []
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation)) #remove punctuation text = text.split(" ") #split words into array for detection.
    text = text.split(" ")

    emotion_arr = [0,0,0,0] #[happy,sad,angry,fearful]
    not_detected = False

    for word in text: #this is to check the emotion currently based of words used
        # count keywords
        if word == "not":
            not_detected = True

        if word in happy_list:
            if not_detected == True:
                emotion_arr[1] += 1
                not_detected = False
            else:
                emotion_arr[0] += 1

        if word in sad_list:
            if not_detected == True:
                emotion_arr[0] += 1
                not_detected = False
            else:
                emotion_arr[1] += 1

        if word in angry_list:
            emotion_arr[2] += 1

        if word in fear_list:
            emotion_arr[3] += 1

    # collate counting, check for when no words detected.
    total = 0
    for emotion_value in emotion_arr:
        total += emotion_value
        emotion = emotion_arr.index(max(emotion_arr)) + 1
    
    if total == 0:
        output.append(0)
    else:
        output.append(emotion)

    ## Recomendations gabriel
    if total == 0: #no emotion detected
        output.append("Well, idk what you're feeling, could you maybe try and use different words to explain you're emotion? ")
        url = ""

    #choose appropriate song and random food for user
    if emotion == 1: #happy
        song_list = list(happysong.keys())
        randoms = song_list[random.randint(0,len(song_list)-1)]
        url = happysong.get(randoms)

        randomf = random.choice(food)
        output.append("Oh, nice! Great that you're feeling happy today \\n\\nbased on your feeling, try listening to {}".format(randoms))
        output.append("At the same time if you're feeling hungry, try making this '{}'".format(randomf))
 
    if emotion == 2: #sad
        song_list = list(sadsong.keys())
        randoms = song_list[random.randint(0,len(song_list)-1)]
        url = sadsong.get(randoms)

        randomf = random.choice(food)
        output.append ("Man, its alright you can get through it.\\n\\nwell because your feeling sad, try listening to {}".format(randoms))
        output.append("At the same time if you're feeling hungry, try making this '{}'".format(randomf))

    if emotion == 3: #angry
        song_list = list(angrysong.keys())
        randoms = song_list[random.randint(0,len(song_list)-1)]
        url = angrysong.get(randoms)

        randomf = random.choice(food)
        output.append("Yea its like that sometimes\\n\\ntry listening to {}".format(randoms))
        output.append("At the same time if you're feeling hungry, try making this '{}'".format(randomf))

    if emotion == 4: #fear
        song_list = list(fearsong.keys())
        randoms = song_list[random.randint(0,len(song_list)-1)]
        url = fearsong.get(randoms)

        randomf = random.choice(food)
        output.append("Oh i see\\n\\nwell, if you're scared, why not listen to {}".format(randoms))
        output.append("At the same time if you're feeling hungry, try making this '{}'".format(randomf))
 
    output.append(url)
    return output
"""
