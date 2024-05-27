import streamlit as st
from PIL import Image
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='pt', target='en')

st.title('Hair Revolution')


st.sidebar.header('Hair Revolution')
st.sidebar.write("O app que vai transformar a sua forma de cuidar do cabelo. Se você é um(a) amante da LÓreal professional esse é o seu site ideal")
foto = Image.open('camz.jpeg') 
st.image(foto, caption="Camila Cabello L'Oreal", width= 500)

with st.form('form'):
    st.header("Tipo de cabelo")
    st.image("tiposdecabelo.png", width=300)
 
    
    tipo_cabelo = st.radio("Qual o seu tipo de cabelo?",
                           ['1', '2A', '2B', '2C', '3A', '3B', '3C', '4A', '4B'],
                          horixontal=True)
    st.header("Cor do cabelo")
    cor_cabelo = st.radio("Qual a cor do seu cabelo?", ['Castanho claro', 'Castanho Escuro', 'Preto', 'Loiro claro', 'Loiro escuro', 'Ruivo', 'Platinado'])
    st.header("Procedimentos")
    procedimentos_cabelo = st.radio("Quais procedimentos você já realizou?", ['Descoloração', 'Tintura', 'Botox', 'Progressiva', 'Outros alisamentos', 'Cabelo virgem'])
    st.header("Genero") 
    genero = st.radio("Selecione seu genero", ['Feminino', 'Masculino', 'Neutro']) 
    st.header("Cor de pele") 
    cor_pele = st.radio("Selecione sua cor de pele", ['Preto', 'Branco', 'Amarelo', 'Indigena', 'Pardo'])
    st.header("Comprimento") 
    comprimento_cabelo = st.radio("Selecione o comprimento do seu cabelo", ['Extra curto', 'Curto', 'Médio', 'Longo', 'Extra longo'])       
    st.header("Características")
    características_cabelo = st.radio("Selecione as característica do seu cabelo", ['Raiz oleosa', 'Ponta seca', 'Seco', 'Oleoso', 'Normal']) 
    botao = st.form_submit_button('enviar') 

if botao: 
    frase = f"uma foto de uma pessoa do genero {genero} com cabelo tipo {tipo_cabelo}, cor de cabelo {cor_cabelo} etc etc etc" 
    st.write(frase)
    st.write(translator.translate(frase))
