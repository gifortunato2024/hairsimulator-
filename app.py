import streamlit as st
import matplotlib.pyplot as plt
import webuiapi
from PIL import Image
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
import numpy as np
import os
import requests

# Configuração
url = 'https://dd02-2804-14d-5c5c-9ce1-00-1004.ngrok-free.app'

### Funções
@st.cache_resource
def load_objects():
    api = webuiapi.WebUIApi(url, port=7860, use_https=True,
                            baseurl=f'{url}/sdapi/v1',
                            sampler='Euler a', steps=30)
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))
    swapper = insightface.model_zoo.get_model('modelo.onnx',download=False,download_zip=False)
    return api, app, swapper

def swap_faces(fake, user, i1=0, i2=0):
    img1 = cv2.imread(fake)
    img2 = cv2.imread(user)
    face1 = app.get(img1)[i1]
    face2 = app.get(img2)[i2]
    img1_swapped = swapper.get(img1, face1, face2, paste_back=True)
    return img1_swapped

@st.spinner('Gerando imagem...')
def generate_image(tipo, cor, pele, genero):
    prompt = f'a photo of a {genero_translation[genero]} with {cor_translation[cor]} {tipo_translation[tipo]} hair and {pele_translation[pele]} skin, looking at the camera, Fujifilm X-T4, photography, canon, Fujifilm, realistic, 4k, 8k'
    user = Image.open('user.jpg')
    result_gen = api.img2img(images=[user], prompt=prompt,
                             negative_prompt='painting, sketches, drawing, cartoon, anime, deformed, malformed, ugly, worst quality, bad quality, disfigured, graphite, abstract glitch, text, mutated text',
                             width=1024, height=1024,
                             cfg_scale=7, denoising_strength=0.8,
                             inpaint_full_res=0, inpaint_full_res_padding=32, inpainting_fill=1,
                             inpainting_mask_invert=0, mask_blur=4, restore_faces=True,
                             save_images=True, send_images=True,
                             override_settings={"face_restoration": True, "face_restoration_model": "GPFGAN"},
                             steps=25)
    result_gen.image.save('fake.jpg')

    result_swap = swap_faces('fake.jpg', 'user.jpg')
    plt.imsave('new.jpg', result_swap[:, :, ::-1])

### APP
st.set_page_config(layout="centered", page_title='Hair Simulator', page_icon='🪞')

# Baixa o modelo de outro lugar, caso ele não exista na pasta.
url_modelo = 'https://huggingface.co/mateuspestana/hairsimulator/resolve/main/modelo.onnx'
if not os.path.exists('modelo.onnx'):
    with st.spinner('Baixando modelo...'):
        r = requests.get(url_modelo)
        with open('modelo.onnx', 'wb') as f:
            f.write(r.content)

st.title('Hair Revolution')
st.subheader("O app que vai transformar a sua forma de cuidar do cabelo.")
st.subheader("Se você é um(a) amante da LÓreal professional esse é o seu site ideal")

with st.form(key='infos'):
    st.markdown(''':blue-background[Preencha esse formulário de acordo com as características do seu cabelo]''')
    st.image("Fotoloreal .jpg", width=400)
    form1, form2, form3 = st.columns(3)
    form4, form5, form6 = st.columns(3)
    tipo = form1.selectbox('Tipo de cabelo', ['liso', 'ondulado', 'cacheado', 'crespo'])
    cor = form2.selectbox('Cor do cabelo', ['castanho claro', 'castanho escuro', 'loiro claro', 'loiro escuro', 'ruivo', 'cinza', 'preto', 'platinado', 'outro'])
    pele = form3.selectbox('Cor da pele', ['branca', 'morena', 'preta'])
    genero = form4.selectbox('Gênero', ['homem', 'mulher'])
    procedimentos = form5.multiselect('Procedimentos realizados', ['Descoloração', 'Tintura', 'Botox', 'Progressiva', 'Outros alisamentos'])
    características = form6.selectbox('Característica do seu cabelo', ['Raiz oleosa', 'Ponta seca', 'Seco', 'Oleoso', 'Normal'])
    
    st.divider()
    st.header("Linhas L'Oréal Professionel")
    st.image("Linhassite .jpg", width=680)
    
    # Definindo o caminho das imagens para cada linha
    linhas = [
        {"nome": "Scalp Advanced", "desc": "Cuidados avançados para o couro cabeludo, combatendo problemas como caspa e oleosidade.", "imagem": "Linhassite .jpg"},
        {"nome": "Absolut Repair Molecular", "desc": "Ideal para todos os tipos de cabelo danificados: Garante reconstrução, cabelos mais fortes e nutridos.", "imagem": "Linhassite .jpg"},
        {"nome": "Metal Detox", "desc": "Proteção contra poluentes e impurezas.", "imagem": "Linhassite .jpg"},
        {"nome": "Curl Expression", "desc": "Cuidados especiais para cabelos cacheados, proporcionando definição e controle de frizz.", "imagem": "Linhassite .jpg"},
        {"nome": "Absolut Repair", "desc": "Reparação e nutrição para cabelos danificados, restaurando a saúde e o brilho.", "imagem": "Linhassite .jpg"},
        {"nome": "Choma Creme", "desc": "Tratamento para cabelos coloridos, protegendo a cor e prolongando a intensidade.", "imagem": "Linhassite .jpg"},
        {"nome": "Fluidfier", "desc": "Controle de frizz e definição de cabelos lisos.", "imagem": "Linhassite .jpg"},
        {"nome": "Pro Longer", "desc": "Cuidados para cabelos mais longos, fortalecendo e protegendo as pontas.", "imagem": "Linhassite .jpg"},
        {"nome": "Blondifier", "desc": "Cuidados específicos para cabelos loiros, neutralizando tons amarelados e proporcionando brilho.", "imagem": "Linhassite .jpg"},
        {"nome": "Inforce", "desc": "Fortalecimento e reconstrução para cabelos enfraquecidos e quebradiços.", "imagem": "Linhassite .jpg"},
        {"nome": "Nutrifier", "desc": "Nutrição intensa para cabelos secos e desidratados.", "imagem": "Linhassite .jpg"},
    ]
    
    for linha in linhas:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(linha["imagem"], width=80)  # Ajuste o tamanho conforme necessário
        with col2:
            st.markdown(f'**:{linha["nome"].split()[0].lower()}[{linha["nome"]}:]** {linha["desc"]}')

    linha = st.radio("Escolha a linha que você quer ver o resultado no seu cabelo", [linha["nome"] for linha in linhas])
    
    foto = st.file_uploader('Escolha uma foto', type=['jpg', 'png', 'jpeg'])
    submit = st.form_submit_button('Simular')
# foto = st.camera_input('Tire uma foto')
    foto = st.file_uploader('Escolha uma foto', type=['jpg', 'png', 'jpeg'])
    submit = st.form_submit_button('Simular')
    
# Mapeamento das opções de idioma
tipo_translation = {'liso': 'straight', 'ondulado': 'wavy', 'cacheado': 'curly', 'crespo': 'coily'}
cor_translation = {'castanho claro': 'light brown', 'castanho escuro': 'dark brown', 'loiro claro': 'light blonde', 'loiro escuro': 'dark blonde', 'ruivo': 'red', 'cinza': 'gray', 'preto': 'black', 'platinado': 'platinum', 'outro': 'same as the original picture'}
pele_translation = {'branca': 'white', 'morena': 'tan', 'preta': 'black'}
genero_translation = {'homem': 'man', 'mulher': 'woman'}
    
if submit:
    api, app, swapper = load_objects()
    try:
        # with open(f'user.jpg', 'wb') as f:
        #     f.write(foto.read())
        img = Image.open(foto)
        img = img.resize((img.width // 4, img.height // 4))
        if foto.name[-3:] == 'png':
            img = img.convert('RGB')
        img.save('user.jpg')
        
    except:
        st.error('Erro ao processar foto. Envie novamente.')

    st.write(f'Você escolheu um cabelo {tipo}, cor {cor}, pele {pele} e gênero {genero}')
    try:
        generate_image(tipo, cor, pele, genero)
    except Exception as e:
        st.error('Erro ao gerar a imagem. Tente novamente.')
        st.error(e)

    # col1, col2 = st.columns(2)
    # col1.image(foto, use_column_width=True)
    # col2.image('fake.jpg', use_column_width=True)
    result_swap = swap_faces('fake.jpg', 'user.jpg')
    plt.imsave('new.jpg', result_swap[:, :, ::-1])
    with st.expander('Resultado', expanded=True):
       st.image('new.jpg', width=400)
