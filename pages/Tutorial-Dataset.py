import streamlit as st
import base64
from PIL import Image
from subprocess import STDOUT, check_call


st.title('Cara membuat dataset untuk diprediksi')
st.write('''
    Sebelum mulai, pastikan anda memiliki aplikasi spreadsheet yang mendukung file ekstensi CSV seperti Google Sheet atau Microsoft Excel Original.
''')

st.write('''
    ## Siapkan Data
    ##### Silahkan download templete dibawah ini untuk memudahkan!
''')

st.markdown("""
    [Download Templete](https://github.com/Fisra/PREDIKSI-EPL/raw/main/assets/TEMPLETE.xlsx)
""")

st.write('''
        Setelah mengunduh file diatas, isi data sesuai kolom yang disediakan di templete. Berikut penjelasannya.
        ###### Jumlah Main
        Isi data jumlah main sesuai dengan data sebenarnya. Misal, hingga matchweek 32 80% tim sudah bermain 32 kali sedangkan beberapa masih 31 kali main, tetap tulis apa adanya.
        ###### Jumlah Gol
        Isi semua data gol baik dari gol home maupun gol away dari setiap tim hingga di matchweek yang diinginkan. Misal, jika di matchweek 32 Manchester city sudah bermain 31 kali dengan gol kandang 10, sedangkan Arsenal sudah bermain 32 kali dengan gol kandang 15, tulis sesuai dengan apa adanya data.
        ###### Jumlah kebobolan
        Isi semua data kebobolan baik dari kebobolan home maupun kebobolan away dari setiap tim hingga di matchweek yang diinginkan. Misal, jika di matchweek 32 Manchester city sudah bermain 31 kali dengan kebobolan kandang 10, sedangkan Arsenal sudah bermain 32 kali dengan kebobolan kandang 15, tulis sesuai dengan apa adanya data.
        ###### Jumlah Kemenangan
        Total kemenangan yang diraih setiap tim hingga matchweek yang diinginkan.
        ###### Raihan Poin
        Raihan poin yang sudah dikumpulkan setiap tim hingga matchweek yang diinginkan.

''')