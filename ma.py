import streamlit as st

# 画像ファイルの読み込み
from PIL import Image
image = Image.open('you.png')

# ボタンが押されたら実行される関数
def display_text_and_image():
    st.write("テキストが表示されます。")
    st.image(image, caption='画像のキャプション')

# ボタンの作成
if st.button('ボタンを押してください'):
    display_text_and_image()