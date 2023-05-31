
import streamlit as st 
import webbrowser

st.title('申請書')

st.write('DataFrame')

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
    webbrowser.open_new(
        "<https://logoform.jp/f/T64Xk/1145073?key=3af8caf1f2bb0014b0c9b046d1e376f7b8065170617264317f71b981444e9be9>"
        )


if st.button("youtube申請"):
    open_link()

def open_link2():
    webbrowser.open_new(
        "<https://logoform.jp/f/Mc4rD/1159399?key=203cdbdb060f1e9dd3b1519b609a321b13285f51692664ea66c393391bb0b47a>"
        )


if st.button("リーダー研修会Ⅰ"):
    open_link2()
