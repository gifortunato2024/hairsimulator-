import streamlit as st
import matplotlib.pyplot as plt
import webuiapi
from PIL import Image
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
import numpy as np

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
    swapper = insightface.model_zoo.get_model('/Users/mateuspestana/Downloads/inswapper_128.onnx',download=False, download_zip=False)
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
    prompt = f'a photo of a {genero_translation} with {cor_translation} {tipo_translation} hair and {pele_translation} skin, looking at the camera, Fujifilm X-T4, photography, canon, Fujifilm, realistic, 4k, 8k'
    user = Image.open('user.jpg')
    result_gen = api.img2img(images=[user], prompt=prompt,
                             negative_prompt='painting, sketches, drawing, cartoon, anime, deformed, malformed, ugly, worst quality, bad quality, disfigured, graphite, abstract glitch, text, mutated text',
                             width=1024, height=1024,
                             cfg_scale=7, denoising_strength=0.8,
                             inpaint_full_res=0, inpaint_full_res_padding=32, inpainting_fill=1,
                             inpainting_mask_invert=0, mask_blur=4, restore_faces=True,
                             save_images=True, send_images=True, alwayson_scripts={"Extra options": {"args": [True, "GPFGAN"]}},
                             override_settings={"face_restoration": True, "face_restoration_model": "GPFGAN"},
                             steps=25)
    result_gen.image.save('fake.jpg')

    result_swap = swap_faces('fake.jpg', 'user.jpg')
    plt.imsave('new.jpg', result_swap[:, :, ::-1])

### APP
st.set_page_config(layout="centered", page_title='Hair Simulator', page_icon='🪞')

st.title('Hair Revolution')
st.subheader("O app que vai transformar a sua forma de cuidar do cabelo.")
st.caption("Se você é um(a) amante da LÓreal professional esse é o seu site ideal")

with st.form(key='infos'):
    form1, form2, form3, form4, form5, form6 = st.columns(6)
    tipo = form1.selectbox('Tipo de cabelo', ['liso', 'ondulado', 'cacheado', 'crespo'])
    cor = form2.selectbox('Cor do cabelo', ['castanho claro', 'castanho escuro', 'loiro claro', 'loiro escuro', 'ruivo', 'cinza', 'preto', 'platinado', 'outro'])
    pele = form3.selectbox('Cor da pele', ['branca', 'morena', 'preta'])
    genero = form4.selectbox('Gênero', ['homem', 'mulher'])
    procedimentos = form5.multiselect('Procedimentos realizados', ['Descoloração', 'Tintura', 'Botox', 'Progressiva', 'Outros alisamentos'])
    características = form6.selectbox('Característica do seu cabelo', ['Raiz oleosa', 'Ponta seca', 'Seco', 'Oleoso', 'Normal'])
    linha = st.radio("Escolha a linha que você quer ver o resultado no seu cabelo", ['Absolut Repair Molecular', 'Metal Detox', 'Scalp Advanced', 'Curl Expression', 'Absolut Repair', 'Choma Creme', 'Fluidfier', 'Pro Longer', 'Blondifier', 'Inforce', 'Nutrifier'])
    
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

    with open(f'user.jpg', 'wb') as f:
        f.write(foto.read())

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
