# Library
import streamlit as st

# write
st.title('SOFTWARE PERKALIAN')
st.subheader('Ini adalah aplikasi untuk mengalikan bilangan')

#input bil pertama
number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

#input bil kedua
number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

#hasil hitungan
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('Silahkan tekan tombol Hitung')