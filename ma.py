import streamlit as st

st.title('各種申請')
st.subheader('申請するボタンを押してください')


# 画像ファイルの読み込み
from PIL import Image
image = Image.open('yo.png')
image2 = Image.open('re.png')

# ボタンが押されたら実行される関数
def display_text_and_image():
    st.write(
        "<https://logoform.jp/f/T64Xk/1145073?key=3af8caf1f2bb0014b0c9b046d1e376f7b8065170617264317f71b981444e9be9>"
    )
    st.image(image, caption='youtube動画申請',width=200)

# ボタンの作成
if st.button('youtube動画申請'):
    display_text_and_image()
    
    

# ボタンが押されたら実行される関数
def display_text_and_image2():
    st.write(
        "<https://logoform.jp/f/Mc4rD/1159399?key=203cdbdb060f1e9dd3b1519b609a321b13285f51692664ea66c393391bb0b47a>"
    )
    st.image(image2, caption='リーダー研修会Ⅰ',width=200)

# ボタンの作成２
if st.button('リーダー研修会Ⅰ'):
    display_text_and_image2()
    

if st.button('動画'):
   video_file = open('rer.MP4', 'rb')
   video_bytes = video_file.read()

   st.video('rer.MP4', format="video/mp4", start_time=0)