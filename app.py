import streamlit as st 
st.title('hairrevolution') 
with st.sidebar:O
st.header('Hair Revolution')
st.write("O app que vai transformar a sua forma de cuidar do cabelo")
from PIL import Image
foto = Image.open('ariana.hair.jpg')
st.image(foto,
         caption='Logo do Streamlit',
         use_column_width=False)
