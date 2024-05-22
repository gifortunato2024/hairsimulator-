import streamlit as st
from PIL import Image

st.title('Hair Revolution')

st.button("Reset", type="primary")
if st.button("START"):
    st.write(" ")
else:
    st.write("failed")

st.sidebar.header('Hair Revolution')
st.sidebar.write("O app que vai transformar a sua forma de cuidar do cabelo")
foto = Image.open('camz.jpeg') 
st.image(foto, caption="Camila Cabello L'Oreal", width= 500)

st.header("Tipo de cabelo")
st.image("tiposdecabelo.png", width=300)
st.radio("Qual o seu tipo de cabelo?", ['1', '2A', '2B', '2C', '3A', '3B', '3C', '4A', '4B'])
st.header("Cor do cabelo")
st.image("coresdecabelo.png", width=300)
st.radio("Qual a cor do seu cabelo?", ['Castanho claro', 'Castanho Escuro', 'Preto', 'Loiro claro', 'Loiro escuro', 'Ruivo', 'Platinado'])
st.header("Procedimentos")
st.image("virgem.jpg", width=300)
st.radio("Quais procedimentos você já realizou?", ['Descoloração', 'Tintura', 'Botox', 'Progressiva', 'Outros alisamentos', 'Cabelo virgem'])
