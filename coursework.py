
import string #import these things for the code to work
import random
import webbrowser

#jake word detector
def coursework(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation)) #remove punctuation text = text.split(" ") #split words into array for detection.
    text = text.split(" ")

    happy_list = ['great', 'awesome', 'joyful', 'happy', 'glad', 'content', 'acomplished', 'amazing', 'omg', 'okay', 'yippee', 'slay', 'good']
    sad_list = ['down', 'depressed', 'lonely', 'blue', 'heartbroken', 'unhappy', 'gloomy', 'melancholic', 'cry', 'tears', 'sad', 'demoralised', 'hurt', 'defeated', 'dejected', 'stressed', 'bad']
    angry_list = ['angry', 'frustrated', 'annoyed', 'grr', 'grrr', 'furious', 'enraged', 'mad', 'agitated', 'outraged', 'fuming', 'exasperated', 'displeased']
    fear_list = ['fear', 'fearful', 'worry', 'worried', 'afraid', 'terrified', 'anxious', 'nervous', 'scared', 'frightened', 'panick', 'panicking', 'hesitant', 'uneasy', 'tense', 'stammer']
    #^^ list of possible words to give wider variety of options to express themselves
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

    print() #newline
    ## Recomendations gabriel
    #big list ;-; for everything from food to songs url
    food = ["Grilled chicken Breasts", "Vegetable Stir-Fry", "Spaghetti Bolognese", "Baked Salmon", "Quinoa Salad", "Roasted Vegetables", "Chicken Caesar Salad", "Pasta Primavera", "Baked Chicken Thighs", "Caprese Salad","Vegetarian Chili", "Oven-Baked BBQ Chicken", "Egg Fried Rice", "Greek Gyro Wrap", "Mushroom Risotto", "Tacos", "Baked Ziti", "Shrimp Stir-Fry", "Cauliflower Pizza", "Omelette"]
    happysong = {
        "'Happy' by Pharrell Williams": "https://youtu.be/ZbZSe6N_BXs?si=3OJnWTE7pheHdAi2",
        "'Don't Stop Believin' by Journey": "https://youtu.be/1k8craCGpgs?si=BUWPN-9Y8at96Ziz",
        "'Walking on Sunshine' by Katrina and the Waves": "https://youtu.be/iPUmE-tne5U?si=xFuu3xQPnWNkSnr6",
        "'Uptown Funk' by Mark Ronson ft. Bruno Mars": "https://youtu.be/OPf0YbXqDm0?si=aujdLZtYeyJlZylY",
        "'I Gotta Feeling' by The Black Eyed Peas": "https://youtu.be/uSD4vsh1zDA?si=QboSnbhiYaDYWR9S",
        "'Shut Up and Dance' by WALK THE MOON": "https://youtu.be/6JCLY0Rlx6Q?si=vxsMq6_BO6Gk16Ej",
        "'Can't Stop the Feeling!' by Justin Timberlake": "https://youtu.be/ru0K8uYEZWw?si=Gfi9ffD7KOYHYCLj",
        "'Good Vibrations' by The Beach Boys": "https://youtu.be/apBWI6xrbLY?si=BO8Si1ceq5AQuWtP",
        "'Dancing Queen' by ABBA": "https://youtu.be/xFrGuyw1V8s?si=oXAncplsJYegDh-H",
        "'I'm a Believer' by The Monkees": "https://www.youtube.com/watch?v=wB9YIsKIEbA"
    }
    sadsong = {
        "'Lean On Me' by Bill Withers": "https://www.youtube.com/watch?v=fOZ-MySzAac",
        "'Here Comes the Sun' by The Beatles": "https://www.youtube.com/watch?v=GKdl-GCsNJ0",
        "'Three Little Birds' by Bob Marley": "https://www.youtube.com/watch?v=HNBCVM4KbUM",
        "'What a Wonderful World' by Louis Armstrong": "https://www.youtube.com/watch?v=oVv5P_eie4o",
        "'Don't Worry, Be Happy' by Bobby McFerrin": "https://www.youtube.com/watch?v=d-diB65scQU",
        "'Somewhere Over the Rainbow' by Israel Kamakawiwo'ole": "https://www.youtube.com/watch?v=3BeKhlUzPUc",
        "'You've Got a Friend' by James Taylor": "https://www.youtube.com/watch?v=nEFfzHiEKHY",
        "'Count on Me' by Bruno Mars": "https://www.youtube.com/watch?v=6k8cpUkKK4c",
        "'Ain't No Mountain High Enough' by Marvin Gaye and Tammi Terrell": "https://www.youtube.com/watch?v=ABfQuZqq8wg",
        "'Firework' by Katy Perry": "https://www.youtube.com/watch?v=QGJuMBdaqIw",
    }
    angrysong = {
        "'Wish you the worst' by Ryan Mack": "https://www.youtube.com/watch?v=_9bPlmRUq_s",
        "'Weightless' by Marconi Union": "https://www.youtube.com/watch?v=UfcAVejslrU",
        "'Re: Stacks' by Bon Iver": "https://www.youtube.com/watch?v=V9E2E8_Fhto",
        "'3WW' by alt-J": "https://www.youtube.com/watch?v=ZwBkXgWNs_M",
        "'Lost in the Light' by Bahamas": "https://www.youtube.com/watch?v=jPJNt1eTVNY",
        "'Stuck on the Puzzle' by Alex Turner": "https://www.youtube.com/watch?v=TKvzHBdcAdM",
        "'Innerbloom' by RUFUS DU SOL": "https://www.youtube.com/watch?v=Tx9zMFodNtA",
        "'The Night We Met' by Lord Huron": "https://www.youtube.com/watch?v=KtlgYxa6BMU",
        "'Cherry Wine' by Hozier": "https://www.youtube.com/watch?v=SdSCCwtNEjA",
        "'To Build a Home' by The Cinematic Orchestra": "https://www.youtube.com/watch?v=oUFJJNQGwhk",
    }
    fearsong = {
        "'Lean On Me' by Bill Withers" : "https://www.youtube.com/watch?v=fOZ-MySzAac",
        "'Three Little Birds' by Bob Marley" : "https://www.youtube.com/watch?v=HNBCVM4KbUM",
        "'What a Wonderful World' by Louis Armstrong" : "https://www.youtube.com/watch?v=rBrd_3VMC3c",
        "'Don't Worry, Be Happy' by Bobby McFerrin" : "https://www.youtube.com/watch?v=d-diB65scQU",
        "'Here Comes the Sun' by The Beatles" : "https://www.youtube.com/watch?v=KQetemT1sWc",
        "'You've Got a Friend' by James Taylor" : "https://www.youtube.com/watch?v=eAR_Ff5A8Rk",
        "'Bridge Over Troubled Water' by Simon & Garfunkel" :  "https://www.youtube.com/watch?v=4G-YQA_bsOU",
        "'Imagine' by John Lennon" : "https://www.youtube.com/watch?v=YkgkThdzX-8",
        "'I Will Survive' by Gloria Gaynor" : "https://www.youtube.com/watch?v=6dYWe1c3OyU",
        "'Somewhere Over the Rainbow' by Israel Kamakawiwo'ole" : "https://www.youtube.com/watch?v=V1bFr2SWP1I"
    }

    if total == 0: #no emotion detected
        message = ("Well, idk what you're feeling, could you maybe try and use different words to explain you're emotion? ")
        emotion = 0
        url = ""

         #choose appropriate song and random food for user
    #nathan song food selector
    if emotion == 1: #happy
        song_list = list(happysong.keys())
        randoms = song_list[random.randint(0,len(song_list)-1)]
        url = happysong.get(randoms)

        randomf = random.choice(food)
        message = ("Oh, nice! Great that you're feeling happy today \nbased on your feeling, try listening to {} \nAt the same time if you're feeling hungry, try making this '{}'".format(randoms,randomf))

    if emotion == 2: #sad
        song_list = list(sadsong.keys())
        randoms = song_list[random.randint(0,len(song_list)-1)]
        url = sadsong.get(randoms)

        randomf = random.choice(food)
        message = ("Man, its alright you can get through it.\nwell because your feeling sad, try listening to {}\nAt the same time if you're feeling hungry, try making this '{}'".format(randoms,randomf))

    if emotion == 3: #angry
        song_list = list(angrysong.keys())
        randoms = song_list[random.randint(0,len(song_list)-1)]
        url = angrysong.get(randoms)

        randomf = random.choice(food)
        message = ("Yea its like that sometimes\ntry listening to {}\nAt the same time if you're feeling hungry, try making this '{}'".format(randoms,randomf))

    if emotion == 4: #fear
        song_list = list(fearsong.keys())
        randoms = song_list[random.randint(0,len(song_list)-1)]
        url = fearsong.get(randoms)

        randomf = random.choice(food)
        message = ("Oh i see\nwell, if you're scared, why not listen to {}\nAt the same time if you're feeling hungry, try making this '{}'".format(randoms,randomf))

    output = [emotion,message,url]
    return output
