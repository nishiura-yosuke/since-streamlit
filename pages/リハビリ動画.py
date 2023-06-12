import webbrowser
import streamlit as st
import pandas as pd

# CSVファイルを読み込み、Pandas DataFrameに保存する
data = pd.read_csv("リハビリ動画.csv")

# Streamlitアプリを作成する
def app():
    # アプリのタイトルを表示
    st.title("リハビリ動画")

    # レイアウトを調整するためにカラムを使用する
    col1, col2 = st.beta_columns(2)

    # 動画リストを表示する
    for index, row in data.iterrows():
        title = row["タイトル"]
        url = row["URL"]

        # 偶数番目の動画は左側のカラムに、奇数番目の動画は右側のカラムにボタンを配置する
        if index % 2 == 0:
            with col1:
                if st.button(title):
                    # ボタンがクリックされた場合、対応するURLを開く
                   st.video(url)
        else:
            with col2:
                if st.button(title):
                    # ボタンがクリックされた場合、対応するURLを開く
                   st.video(url)

if __name__ == "__main__":
    app()