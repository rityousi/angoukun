# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('時間計測')

import time

 

p = 91
q = 71
n = p*q
e = 17
a = 87
b = 987


 

code_a = pow(a, e, n)
code_b = pow(b, e, n)
    
def gcd(v, w):
       while w:
           v, w = w, v % w
       return v
    
def lcm(v, w):
       return abs(v * w) // gcd(v, w)
    
num1 = p-1
num2 = q-1
r= lcm(num1, num2)
    
def extended_gcd(s, t):
    if t == 0:
        return s, 1, 0
    else:
        d, x, y = extended_gcd(t, s % t)
        return d, y, x - (s // t) * y

def solve_linear_diophantine(s, t, u):
    d, x, y = extended_gcd(s, t)
    if u % d == 0:
        x0 = x * (u // d)
        y0 = y * (u // d)
        if x0 >= 0:
            return x0, y0
        else:
            quotient = (-x0 + abs(t) - 1) // abs(t)
            x = x0 + quotient * (t // d)
            y = y0 - quotient * (s // d)
            return x, y
    else:
        return none

    
s = e
t = -r
u = 1
solution = solve_linear_diophantine(s, t, u)
if solution:
        x, y = solution
        print(f"整数解: x = {x}, y = {y}")
else:
        print('解なし')
        
Pa = pow(code_a,x,n)
Pb = pow(code_b,x,n)
print(Pa,Pb)