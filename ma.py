import imghdr
import streamlit as st 
import numpy as np 
import pandas as pd 
from PIL import Image
import webbrowser

st.title('申請書')

#st.write('DataFrame')

#df = pd.DataFrame(
 #   np.random.rand(100,2)/[50,50]+[35.69,139.70],
 #                 columns=['lat','lon']
 #                 )
#st.map(df)

#st.dataframe(df.style.highlight_max(axis=0))

#st.write('Display Image')


#image = Image.open('IMG_1748.jpeg')

#st.image(image, caption='Sunrise by the mountains')

#if st.button('申請書'):
 #   st.write('Why hello there')
#else:
 #   st.write('Goodbye')
    
#if st.button('申請書２'):
 #   st.write('Why hello there')
#else:
 #   st.write('Goodbye')

def open_link():
    webbrowser.open_new("<https://www.google.com>")


if st.button("youtube申請"):
    open_link()

def open_link2():
    webbrowser.open_new("<https://www.apple.com>")


if st.button("個人ファイル保存申請"):
    open_link2()
