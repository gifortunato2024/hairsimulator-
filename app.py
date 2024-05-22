import streamlit as st
from PIL import Image

st.title('Hair Revolution')

st.sidebar.header('Hair Revolution')
st.sidebar.write("O app que vai transformar a sua forma de cuidar do cabelo")
foto = Image.open('camz.jpeg') 
st.image(foto, caption="Camila Cabello L'Oreal", width= 500)
tab1, tab2, tab3 = st.tabs(["Tipo de cabelo", "Cor do cabelo", "Procedimentos"])

with tab1:
   st.header("Qual o seu tipo de cabelo?")
   st.image("tiposdecabelo.png", width=300)

with tab2:
   st.header("Qual a cor do seu cabelo?")
   st.image("coresdecabelo.png", width=300)

with tab3:
   st.header("Quais procedimentos você já realizou?")
   st.image("virgem.jpg", width=200)
