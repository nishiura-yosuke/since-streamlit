
import streamlit as st 
import webbrowser

st.title('申請書')


def open_link():
    webbrowser.open_new(
        "<https://logoform.jp/f/T64Xk/1145073?key=3af8caf1f2bb0014b0c9b046d1e376f7b8065170617264317f71b981444e9be9>"
        , new=0, autoraise=True)


if st.button("youtube申請"):
    open_link()

def open_link2():
    webbrowser.open_new(
        "<https://logoform.jp/f/Mc4rD/1159399?key=203cdbdb060f1e9dd3b1519b609a321b13285f51692664ea66c393391bb0b47a>"
        , new=0, autoraise=True)


if st.button("リーダー研修会Ⅰ"):
    open_link2()


def open_website():
    webbrowser.open_new_tab(
        "<https://logoform.jp/f/Mc4rD/1159399?key=203cdbdb060f1e9dd3b1519b609a321b13285f51692664ea66c393391bb0b47a>"

        )

if st.button('Webページを開く'):
    open_website()
