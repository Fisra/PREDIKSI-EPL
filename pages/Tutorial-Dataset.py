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

st.download_button(label='Download Templete', 
                   data=TES_AJA.csv,
                   mime = 'text/csv'
                   )

st.write('''
        Setelah mengunduh file diatas, isi data sesuai kolom yang disediakan di templete
''')