
import streamlit as st 
from PIL import Image


st.title('申請書')




if st.button("youtube申請"):
    st.write(
        "<https://logoform.jp/f/T64Xk/1145073?key=3af8caf1f2bb0014b0c9b046d1e376f7b8065170617264317f71b981444e9be9>"
      )
    
    image = Image.open('you.png')

    st.image(image, caption='QRコード')


if st.button('リーダー研修会Ⅰ'):
    st.write(
        "<https://logoform.jp/f/Mc4rD/1159399?key=203cdbdb060f1e9dd3b1519b609a321b13285f51692664ea66c393391bb0b47a>"
             
             )
