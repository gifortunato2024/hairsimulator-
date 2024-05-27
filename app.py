import streamlit as st
from PIL import Image

st.title('Hair Revolution')


st.sidebar.header('Hair Revolution')
st.sidebar.write("O app que vai transformar a sua forma de cuidar do cabelo.
Se você é um(a) amante da LÓreal professional esse é o seu site ideal")
foto = Image.open('camz.jpeg') 
st.image(foto, caption="Camila Cabello L'Oreal", width= 500)

with st.form('form'):
    st.header("Tipo de cabelo")
    st.image("tiposdecabelo.png", width=300)
    st.radio("Qual o seu tipo de cabelo?", ['1', '2A', '2B', '2C', '3A', '3B', '3C', '4A', '4B'])
    st.header("Cor do cabelo")
    st.radio("Qual a cor do seu cabelo?", ['Castanho claro', 'Castanho Escuro', 'Preto', 'Loiro claro', 'Loiro escuro', 'Ruivo', 'Platinado'])
    st.header("Procedimentos")
    st.radio("Quais procedimentos você já realizou?", ['Descoloração', 'Tintura', 'Botox', 'Progressiva', 'Outros alisamentos', 'Cabelo virgem'])
    botao = st.form_submit_button('enviar') 
