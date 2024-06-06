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
    st.image("Fotoloreal .jpg", width=400)
    tipo_cabelo = st.radio("Qual o seu tipo de cabelo?",  ['1', '2A', '2B', '2C', '3A', '3B', '3C', '4A', '4B'],
                          horizontal=True)
    st.header("Cor do cabelo")
    cor_cabelo = st.radio("Qual a cor do seu cabelo?", ['Castanho claro', 'Castanho Escuro', 'Preto', 'Loiro claro', 'Loiro escuro', 'Ruivo', 'Platinado'], 
                          horizontal=True)
    st.header("Procedimentos")
    procedimentos_cabelo = st.radio("Quais procedimentos você já realizou?", ['Descoloração', 'Tintura', 'Botox', 'Progressiva', 'Outros alisamentos', 'Cabelo virgem'],
                                   horizontal=True)
    st.header("Gênero") 
    genero = st.radio("Selecione seu gênero", ['Feminino', 'Masculino', 'Neutro'],
                     horizontal=True) 
    st.header("Cor de pele") 
    cor_pele = st.radio("Selecione sua cor de pele", ['Preto', 'Branco', 'Amarelo', 'Indigena', 'Pardo'],
                       horizontal=True)
    st.header("Comprimento") 
    comprimento_cabelo = st.radio("Selecione o comprimento do seu cabelo", ['Extra curto', 'Curto', 'Médio', 'Longo', 'Extra longo'],
                                 horizontal=True)       
    st.header("Características")
    características_cabelo = st.radio("Selecione as característica do seu cabelo", ['Raiz oleosa', 'Ponta seca', 'Seco', 'Oleoso', 'Normal'],
                                     horizontal=True) 
    st.subheader("Opções")
    opções_cabelo = st.radio("Selecione as seguintes opções que o seu cabelo está aparentando", ['Ponta dupla', 'Frizz', 'Poroso', 'Queda', 'Quebra', 'Crescimento tardio', 'Caspa'],
                            horizontal=True) 

    linha = st.radio("Escolha a linha que você quer ver o resultado no seu cabelo",  st.image("Fotoslinhas.jpg", width=400) ['Absolut Repair Molecular', 'Metal Detox', 'Scalp Advanced', 'Curl Expression', 'Absolut Repair', 'Choma Creme', 'Fluidfier', 'Pro Longer', 'Blondifier', 'Inforce', 'Nutrifier'])
    
    botao = st.form_submit_button('enviar') 

if botao: 
    frase = f"uma foto de uma pessoa do genero {genero} com cabelo tipo {tipo_cabelo}, cor de cabelo {cor_cabelo} etc etc etc" 
    st.write(frase)
    st.write(translator.translate(frase))

picture_user = st.camera_input("Tire uma foto do seu rosto com o cabelo para frente, boa iluminação e um fundo neutro")
if picture_user:
    st.image(picture_user)
