import imghdr
import streamlit as st 
import numpy as np 
import pandas as pd 
from PIL import Image

st.title('超入門')

st.write('DataFrame')

#df = pd.DataFrame(
 #   np.random.rand(100,2)/[50,50]+[35.69,139.70],
 #                 columns=['lat','lon']
 #                 )
#st.map(df)

#st.dataframe(df.style.highlight_max(axis=0))

st.write('Display Image')

Image.open('ee.png')

st.image(image,caption='サンプル',use_column_width=True)


