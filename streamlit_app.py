import streamlit as st

from coursework.coursework import coursework
from capitaliser.capitaliser import capitaliser

st.title("ying bing loves a math!!!!11!11!!")
st.write("das so cool")

option = st.checkbox("click 4 A1 math")
if option == True:
    st.write("user has been bleesed with a1")

# text capitalizer
st.write("---")

st.subheader("funny text capitalizer")
prompt_capitaliser = st.text_input("input here: ",value="hee hee heeeee haweeeeeewwww")
word = capitaliser(prompt_capitaliser)
st.write(word)

# coursework
st.write("---")

st.subheader("Coursework wooo")
prompt_coursework = st.text_input("input here:",value= "im very happy :)")

# output format [emotion, message1, massage2, url]
output = coursework(prompt_coursework)

if output[0] == 0:
    st.write(output[1])

else:
    st.write(output[1])
    st.link_button("Play video",output[3])
    st.write(output[2])

# link to github
st.write("---")

st.subheader("The github")
st.link_button("Github :100:","https://github.com/Jakeboiegg/st-testing.git")
