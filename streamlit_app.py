import streamlit as st
import random

st.title("ying bing loves a math!!!!11!11!!")
st.write("das so cool")

option = st.checkbox("click 4 A1 math")
if option == True:
    st.write("user has been bleesed with a1")

# text capitalizer
st.write("\n\n")

st.subheader("funny text capitalizer")
prompt = st.text_input("input here: ")
prompt = list(prompt)

word = []
for chr in prompt:

    rand = random.randint(0,1)
    if rand == 0: chr = chr.lower()
    if rand == 1: chr = chr.upper()
    
    word.append(chr)

word = "".join(word)
st.write(word)
