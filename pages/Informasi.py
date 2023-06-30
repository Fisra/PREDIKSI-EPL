import streamlit as st
from PIL import Image

image1 = Image.open('sejarah-liga-inggris.jpg')
image2 = Image.open('liverpool.jpg')

st.title('Prediksi Juara English Premier League dengan Random Forest')
st.text('Oleh Fisra Keliwawa')
st.header('Tentang EPL')
st.image(image1,'Tropi Liga Inggris')
st.markdown('''
    English Premier League atau lebih dikenal sebagai EPL merupakan kompetisi liga Inggris divisi pertama. Kompetisi ini pertama kali diadakan pada tahun 1888 namun resmi berformat liga pada tahun 1992. Sebelumnya kompetisi ini disebut Football League First Division.
''')
st.subheader('Klub Inggris Tersukses Berdasarkan Title yang didapatkan')
st.image(image2,'Parade Juara di kota Liverpool')
st.markdown('''
    Berdasarkan torehan tropi dan gelar yang dimiliki. Liverpool merupakan klub dari Inggris yang paling sukses. Liverpool merupakan tim yang sejak lama bertengger di divisi utama dan acap kali menjadi kebanggaan inggris di kanca Eropa. Total tropi yang dimiliki liverpool saat ini berjumlah 70. Liverpool saat website ini dibuat diasuh oleh Jurgen Klopp yang merupakan pelatih asal Jerman. Pada masa asuhan Klopp, Liverpool sukses mendapatkan 7 tropi (2022).
    
    Selain itu, Manchester United yang juga salah satu klub tersukses dari Inggris dan saat ini menjadi pemegang gelar juara EPL terbanyak sejumlah 20 tropi.
''')
st.header('Data Mining')
st.markdown('''
    Data mining adalah proses mencari pola-pola tersembunyi berupa penemuan peluang/pengetahuan (knowledge discovery) yang tidak diketahui sebelumnya menggunakan teknik statistik, matematika, kecerdasan buatan untuk mengekstraksi dan mengidentifikasi informasi yang bermanfaat dan pengetahuan yang terkait dari berbagai data dalam jumlah besar.


    Dengan mengolah data dan melakukan perhitungan yang matang, kita dapat memprediksi suatu kejadian, termasuk prediksi juara liga berdasarkan pola yang sang juara di musim-musim sebelumnya.
''')
st.subheader('Teknik Klasifikasi')
st.markdown('''
    Teknik klasifikasi (Classification Technique) merupakan salah satu teknik yang dapat dilakukan dalam proses data mining, dan teknik ini yang akan digunakan untuk memprediksi klub yang akan juara, masuk zona eropa, aman, dan yang berpotensi degradasi. 
    
    Berbagai macam algoritma yang dapat digunakan untuk klasifikasi seperti algortima K-Nearest Neighbour yang mengklasifikasi berdasarkan posisi data dalam matrik dimensinya, Support Vektor Machine yang menggunakan pembatas untuk membedakan data satu dengan yang lainnya, Neural Network yang meniru cara syaraf manusia membedakan sesuatu, serta masih banyak lagi termasuk algoritma Random Forest yang menjadi pilihan algoritma untuk menentukan klasemen EPL.  
''')
st.subheader('Random Forest')
st.markdown('''
    Random Forest adalah algoritma yang mengambil keputusan berdasarkan pohon keputusan (decision tree) dengan cara memilih satu diantara beberapa hal berdasarkan prioritas atribut terbaik dalam jumlah yang besar dan berulang. Algoritma ini kami pilih berdasarkan pengujian dengan algoritma yang menunjang perhitungan probabilitas atau persentase kemungkinan suatu item diklasifikasikan dengan setiap kelas. Algoritma penguji atau kandidat sebelumnya adalah algoritma Support Vektor Machine. ALgoritma ini memiliki akurasi yang cukup lebih baik dibanding Random Forest, namun hasil trainingnya sangat fluktuatif dan perubahan yang terjadi pada data sangat mempengaruhi hasil, sehingga algoritma ini terkesan lebih cocok untuk klasifikasi dibandingkan prediksi. 

    Contoh sederhananya, jika menggunakan SVM kemudian kita berikan ciri ciri hujan SVM akan mengklasifikasikan hujan, sedangkan yang kita inginkan adalah cuaca setelah hujan. Random Forest akan lebih cocok karena prosesnya yang memilah attribut terbaik berdasarkan keadaan training. 
''')
st.header('Proses Data Mining')
st.markdown('''
    Tujuan utama dari data mining bukanlah menghasilkan hasil prediksi terbaik karena itu dilakukan dalam proses machine learning. Tujuan utama dari data mining adalah menghasilkan informasi berguna sebanyak banyaknya.

    Dalam melakukan data mining, terdapat beberapa metode populer yang bisa dipilih seperti KDD (Knowledge Discovery in Database), CRISP-DM (Cross-Industry Standard Process for Data Mining), dan SEMMA. Pada Proses data mining prediksi ini, kami menggunakan metode KDD karena lebih cocok untuk tahap pembelajaran.

    dalam KDD, terdapat langkah langkah sebagai berikut.
    1. Selection
    2. Preprocessing
    3. Transformation
    4. Data Mining
    5. Evaluation

''')
st.subheader('Pengumpulan dan penyusunan dataset klasemen EPL dari tahun ke tahun')
st.markdown('''
    Tahap 1-3 merupakan tahap untuk menyusun dan mempersiapkan dataset yang akan dilatih dan di uji. dalam konteks ini, data yang kami kumpulkan berasal dari berbagai macam sumber terpercaya seperti website resmi EPL, UEFA, dan Besoccer. Data terkumpul dan dihitung berdasarkan gol home dan away, kebobolan home dan away, jumlah poin terkumpul, dan persentase kemenangan yang kemudian dilakukan perhitungan rahasia untuk menghasilkan angka yang melambangkan keadaan klub saat itu dan yang akan terjadi saat itu. 
''')
st.subheader('Pemilihan Algoritma dan pemodelan')
st.markdown('''
    Tahap 4-5 merupakan tahap untuk menyusun, melatih, menguji dan mengevaluasi model yang kita gunakan untuk prediksi. Data yang sudah disusun dalam bentuk CSV akan dimasukkan kedalam model dan dibagi untuk data latih dan data uji yang kemudian menghasilkan laporan yang bisa diambil informasinya. Dalam hal ini, pihak klub tentu dapat mengambil kesimpulan berdasarkan keadaan klub pada sistem prediksi seperti keputusan untuk rotasi pemain, waktunya untuk bermain serius, waktunya menguji lini serang atau lini bertahan, dan masih banyak lagi tergantung perspektif pengguna.
''')
st.header('Membuat Dataset sendiri')
st.markdown('''
    Jika anda ingin menguji juga, anda dapat menyiapkan data sesuai templete yang kami sediakan, silahkan download dan isi sesuai keadaan klasemen pada matchweek pilihan anda.
''')




hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
