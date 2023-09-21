# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('時間計測')

p = 3
q = 5
r = 11
g = 7
n = p * q * r * g
e = 7
a = 29
b = 23

 

 

 

 

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
num3 = r-1
num4 = g-1
z= lcm(lcm(lcm(num1, num2),num3), num4)
    
def extended_gcd(s, t):
        if s == 0:
          return t, 0, 1
          return t, 0, 1
        gcd, x1, y1 = extended_gcd(t % s, s)
        x = y1 - (t // s) * x1
        y = x1
        return gcd, x, y
        
def solve_diophantine_equation(s, t, u):
       gcd, x0, y0 = extended_gcd(abs(s), abs(t))
       if u % gcd != 0:
           return None  
       sign_s = -1 if s < 0 else 1
       sign_t = -1 if t < 0 else 1
       x0 *= sign_s
       y0 *= sign_t
       c0 = u // gcd
       return x0 * c0, y0 * c0
    
s = e
t = -z
u = 1
solution = solve_diophantine_equation(s, t, u)
if solution:
        x, y = solution
        st.write(f"整数解: x = {x}, y = {y}")
else:
        st.write('解なし')
        
Pa = pow(code_a,x,n)
Pb = pow(code_b,x,n)
st.write(Pa,Pb)