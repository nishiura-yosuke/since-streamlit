
import streamlit as st 
from PIL import Image

st.title('申請書')


image = Image.open('you.png')

# ボタンが押されたら実行される関数
def display_text_and_image():
    st.write(
        "<https://logoform.jp/f/Mc4rD/1159399?key=203cdbdb060f1e9dd3b1519b609a321b13285f51692664ea66c393391bb0b47a>"
    
             )
    st.image(image, caption='画像のキャプション')

# ボタンの作成
if st.button('ボタンを押してください'):
    display_text_and_image()