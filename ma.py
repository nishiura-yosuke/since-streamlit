
import streamlit as st 
from PIL import Image

st.title('申請書')

# ボタンの作成
if st.button('ボタンを押してください'):
  image = Image.open('you.png')
  st.image(image, caption='画像のキャプション')

