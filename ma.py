import streamlit as st

st.title('各種申請')
st.subheader('申請するボタンを押してください')

# 画像ファイルの読み込み
from PIL import Image
image = Image.open('you.png')

# ボタンが押されたら実行される関数
def display_text_and_image():
    st.write(
        "<https://logoform.jp/f/T64Xk/1145073?key=3af8caf1f2bb0014b0c9b046d1e376f7b8065170617264317f71b981444e9be9>"
    )
    st.image(image, caption='youtube動画申請',width=200)

# ボタンの作成
if st.button('youtube動画申請'):
    display_text_and_image()
    
    image2 = Image.open('you.png')

# ボタンが押されたら実行される関数
def display_text_and_image2():
    st.write(
        "<https://logoform.jp/f/T64Xk/1145073?key=3af8caf1f2bb0014b0c9b046d1e376f7b8065170617264317f71b981444e9be9>"
    )
    st.image(image2, caption='youtube動画申請',width=200)

# ボタンの作成２
if st.button('リーダー研修会Ⅰ'):
    display_text_and_image2()