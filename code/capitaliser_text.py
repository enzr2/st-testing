text = """
import random

def capitaliser(prompt):
    prompt = list(prompt)
    word = []

    for chr in prompt:
        rand = random.randint(0,1)
        if rand == 0: chr = chr.lower()
        if rand == 1: chr = chr.upper()
        
        word.append(chr)

    word = "".join(word)
    return word
"""
