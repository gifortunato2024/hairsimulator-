import streamlit as st 
st.title('hairrevolution') 
with st.sidebar:
st.header('O aplicativo que revoluciona a forma de cuidar do cabelo')
from PIL import Image
foto = Image.open('ariana.hair.jpg')
st.image(foto,
         caption='Logo do Streamlit',
         use_column_width=False)
