import streamlit as st
import random

from coursework import coursework

st.title("ying bing loves a math!!!!11!11!!")
st.write("das so cool")

option = st.checkbox("click 4 A1 math")
if option == True:
    st.write("user has been bleesed with a1")

# text capitalizer
st.write("---")

st.subheader("funny text capitalizer")
prompt = st.text_input("input here: ",value="hee hee heeeee haweeeeeewwww")
prompt = list(prompt)

word = []
for chr in prompt:

    rand = random.randint(0,1)
    if rand == 0: chr = chr.lower()
    if rand == 1: chr = chr.upper()
    
    word.append(chr)

word = "".join(word)
st.write(word)

# coursework
st.write("---")

st.subheader("Coursework wooo")
prompt2 = st.text_input("input here:",value= "im very happy :)")

output = coursework(prompt2)
if output[0] == 0:
    st.write(output[1])

else:
    st.write(output[1])
    st.link_button("Play video",output[2])

# link to github
st.write("---")

st.subheader("The github")
st.link_button("Github :100:","https://github.com/Jakeboiegg/st-testing.git")
