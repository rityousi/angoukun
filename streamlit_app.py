# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")


    

import streamlit as st
import time
import math
import random

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def prime_game():
    st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Allow the user to make up to 5 guesses
    for i in range(5):
        guess = st.number_input(f"Guess #{i+1}", min_value=1, max_value=100)
        if guess == number_to_guess:
            st.write("Congratulations! You guessed the number!")
            return
        elif guess < number_to_guess:
            st.write("Too low! Try again.")
        else:
            st.write("Too high! Try again.")
    
    # If the user hasn't guessed the number after 5 tries, reveal the answer
    st.write(f"Sorry, you didn't guess the number. The number was {number_to_guess}.")

def main():
    st.title("素因数分解時間計測アプリ")
    st.write("このアプリは、与えられた整数の素因数分解を行い、所要時間を計測します。")
    st.write("また、1から100までの数字を当てるゲームもプレイできます。")
    option = st.selectbox("どちらの機能を使いますか？", ("素因数分解", "数字当てゲーム"))
    if option == "素因数分解":
        number_to_factorize = st.number_input("素因数分解対象の数を入力してください:", min_value=1)
        if st.button("1回計測"):
            start_time = time.time()
            factors = factorize(number_to_factorize)
            end_time = time.time()
            elapsed_time = end_time - start_time
            st.write(f"素因数分解結果: {factors}")
            st.write(f"素因数分解にかかる時間: {elapsed_time:.4f} 秒")
        if st.button("30回計測"):
            elapsed_times = []
            for i in range(30):
                start_time = time.time()
                factors = factorize(number_to_factorize)
                end_time = time.time()
                elapsed_time = end_time - start_time
                elapsed_times.append(elapsed_time)
            avg_elapsed_time = sum(elapsed_times) / len(elapsed_times)
            st.write(f"素因数分解結果: {factors}")
            st.write(f"素因数分解にかかる平均時間: {avg_elapsed_time:.4f} 秒")
    else:
        prime_game()

if __name__ == "__main__":
    main()