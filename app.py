import streamlit as st
from PIL import Image

st.title('Hair Revolution')

st.sidebar.header('Hair Revolution')
st.sidebar.write("O app que vai transformar a sua forma de cuidar do cabelo")
foto = Image.open('camz.jpeg') 
st.image(foto, caption='Camila Cabello L'óreal Paris', width= 500)
