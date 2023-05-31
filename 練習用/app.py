import streamlit as st 

st.title('サンプル')
st.caption('初めてのサンプル')

st.subheader('自己紹介')
st.text('練習中')

code = '''
import streamlit as st 
st.title('サンプル')
'''
st.code(code,language='python')

#画像
image = Image.open('生６.png')
st.image(image,width = 200)
