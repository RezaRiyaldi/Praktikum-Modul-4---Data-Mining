import pickle
import streamlit as st
import pandas as pd
import time

model = pickle.load(open('estimate_cars.sav', 'rb'))

st.title("Estimasi Harga Mobil Bekas")


# Input in Sidebar
st.sidebar.title("Form Input Untuk Spesifikasi Mobil Bekas")
year = st.sidebar.number_input('Tahun Mobil', value=2019)
mileage = st.sidebar.number_input('KM Mobil', value=5000)
tax = st.sidebar.number_input('Pajak Mobil', value=145)
mpg = st.sidebar.number_input('Konsumsi BBM Mobil', value=30.2)
engineSize = st.sidebar.number_input('Uk. Mesin Mobil', value=2)

predict = ''
if (st.sidebar.button('Hitung Estimasi Harga', type='primary')) :
    predict = model.predict([
        [year, mileage, tax, mpg, engineSize]
    ])

    st.write("Dari spesifikasi yang anda berikan sebagai berikut:")
    data = {
        'Tahun' : [year],
        'Kilometer' : [mileage],
        'Pajak': [tax],
        'Konsumsi Bahan Bakar': [mpg],
        'Uk. Mesin' : [engineSize]
    }

    df = pd.DataFrame(data).round(2).astype(str).replace('\.0+$', '', regex=True)
    st.table(df)

    # Konversi mata uang dari Pound to Idr
    pound = 18_444 # 13/04/2023
    idr = format(predict[0] * pound, ',.0f')

    st.subheader(f'Maka estimasi harga mobil `Rp. {idr},-`')
    
    with st.spinner("Tugas ini dipersembahkan oleh: "):
        time.sleep(5)
        st.write("Tugas ini dipersembahkan oleh: ")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image('img/reza.png', caption="Reza Riyaldi", use_column_width=True)
        with col2:
            st.image('img/diki.png', caption="Diki Ramdhani", use_column_width=True)
        with col3:
            st.warning("1 Lagi masih afk")
            # st.image('img/reza.png', caption="Reza Riyaldi", use_column_width=True)

