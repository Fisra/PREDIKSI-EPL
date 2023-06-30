# Import library yang dibutuhkan
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image



data = pd.read_csv('assets/TES_BARU.csv')
data = data.dropna()
# Membagi data menjadi data latih dan data uji
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# Inisialisasi model Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=4, class_weight='balanced')

X_train_team = X_train.iloc[:, :1]
X_test_team = X_test.iloc[:, :1]
X_train_new = X_train.iloc[:, 2:]
X_test_new = X_test.iloc[:, 2:]

# Melatih model dengan data train
rf.fit(X_train_new, y_train)

# Prediksi dengan data test
y_pred = rf.predict(X_test_new)

# Evaluasi performa model
print("Akurasi: ", rf.score(X_test_new, y_test))

st.title('Prediksi Juara English Premier League dengan Random Forest')  
st.text('Oleh Fisra Keliwawa dan Erlan Loanel')

image1 = Image.open('assets/1.png')
image2 = Image.open('assets/notfound.png')
st.image(image1, caption='Source: Pinterest')

#matchweek
week = jumlah = st.text_input('Matchweek','30')
# input url
url = title = st.text_input('Link Dataset')

if 'https://drive.google.com/' in url:
    file_id = url.split('/')[-2]
    read_url='https://drive.google.com/uc?id=' + file_id

    coba = pd.read_csv(read_url)

    nama = coba.iloc[:, 0]

    coba = coba.iloc[:, 1:]

    proba = rf.predict_proba(coba)
    proba = proba*100
    label = ['Juara','Eropa','Aman','Degradasi']
    hasil_baru = pd.DataFrame(proba,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],label)

    klasifikasi = pd.DataFrame(rf.predict(coba),columns=['Klasifikasi'])

    gabung_data = pd.concat([nama,coba,hasil_baru,klasifikasi],axis=1)

    df_sorted = gabung_data.sort_values(['Klasifikasi','Juara', 'Eropa', 'Aman', 'Degradasi'], ascending=[True, False, False, False, False])

    # inisialisasi nama kolom baru
    kata = 'Prediksi Klasemen akhir berdasarkan Matchweek ' + week
    st.subheader(kata)
    st.dataframe(df_sorted)
    st.write("Akurasi: {:.2f}".format(rf.score(X_test_new, y_test)*100),"%")

    st.subheader('Mana Tim Kamu?')
    tim = st.text_input('Nama Tim Sesuai inisial data','')
    if(tim in np.array(df_sorted.iloc[:,0])):
        data = np.array(df_sorted[nama == tim])
        nama_tim = data[0,0]
        HEA = data[0,1]
        AAA = data[0,2]
        AEA = data[0,3]
        
        st.text('Detail Tim')
        st.text('Nama Tim: ' + nama_tim + '(inisialisasi)')
        st.text('Nilai HEA: ') 
        st.text(HEA)

    elif(tim == ''):
        st.image(image2)
    else:
        st.image(image2)
    
else:
    st.image(image2)

# hide_menu_style = """
#     <style>
#     #MainMenu {visibility: hidden;}
#     </style>
#     """
# st.markdown(hide_menu_style, unsafe_allow_html=True)