import streamlit as st
from PIL import Image

st.title('Hair Revolution')

st.sidebar.header('Hair Revolution')
st.sidebar.write("O app que vai transformar a sua forma de cuidar do cabelo")

foto = Image.open('ariana.hair.jpg') 
st.image(foto, caption='Logo do Streamlit', use_column_width=False)
