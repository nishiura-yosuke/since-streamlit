import streamlit as st

# 動画１から動画１０までのURLをリストにまとめる
videos = [
    "<https://www.youtube.com>",
    "<https://www.youtube.com>",
    "<https://www.youtube.com>",
]

# ボタンをクリックした時に指定のURLを開く
def open_url(url):
    js = f"window.open('{url}')"  # JavaScriptを生成
    html = f"<script>{js}</script>"  # HTMLに埋め込む
    st.markdown(html, unsafe_allow_html=True)  # 表示

# 動画ごとにボタンを作成
for i, video in enumerate(videos):
    st.video(f"動画{i+1}")  # 動画を表示
    button = st.button("URLを開く")  # ボタンを作成
    if button:
        open_url(video)  # ボタンをクリックしたらURLを開く

