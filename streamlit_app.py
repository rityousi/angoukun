# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

import sympy

 

def main():
    st.title("大きな数の素因数分解アプリ")

 

    st.write("このアプリは、与えられた整数の素因数分解を行います。")

 

    number_to_factorize = st.number_input("素因数分解対象の数を入力してください:", min_value=1)

 

    if st.button("素因数分解開始"):
        try:
            factors = sympy.factorint(number_to_factorize)
            st.write(f"素因数分解結果: {factors}")
        except Exception as e:
            st.write(f"エラー: {e}")

 

if __name__ == "__main__":
    main()