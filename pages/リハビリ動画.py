import webbrowser
import streamlit as st
import pandas as pd

# CSVファイルを読み込み、Pandas DataFrameに保存する
data = pd.read_excel("リハビリ動画.xlsx")

# Streamlitアプリを作成する
def app():
    st.title("リハビリ動画")

    # 動画リストを表示する
    for index, row in data.iterrows():
        title = row["タイトル"]
        url = row["URL"]
        if st.button(title):
            webbrowser.open_new_tab(url)

if __name__ == "__main__":
    app()