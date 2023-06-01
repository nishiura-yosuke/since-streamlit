
import streamlit as st 
from PIL import Image

st.title('申請書')

image = Image.open('you.png')
st.image(image, caption='画像のキャプション')

