import streamlit as st

st.title('シャント動画')
   
if st.button('動画2'):

   st.video('https://youtu.be/XbQ06MScArk', format="video/mp4", start_time=0)
   
if st.button('動画3'):

   st.video('https://youtu.be/RYcr48VCNjs', format="video/mp4", start_time=0)
