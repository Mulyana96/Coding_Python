import streamlit as st

# Judul aplikasi
st.title("Aplikasi Kalkulator Berbasis Web")
st.write("Aplikasi ini dibuat untuk memudahkan pekerjaan.")

# Sidebar untuk memilih operasi
st.sidebar.header("Pilih Operasi")
operation = st.sidebar.selectbox(
    "Operasi Matematika",
    ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"]
)

# Input angka
st.subheader("Input Angka")
num1 = st.number_input("Masukkan angka pertama", value=0.0, step=1.0)
num2 = st.number_input("Masukkan angka kedua", value=0.0, step=1.0)

# Tombol untuk melakukan perhitungan
if st.button("Hitung"):
    result = None
    if operation == "Penjumlahan":
        result = num1 + num2
        st.success(f"Hasil Penjumlahan: {result}")
    elif operation == "Pengurangan":
        result = num1 - num2
        st.success(f"Hasil Pengurangan: {result}")
    elif operation == "Perkalian":
        result = num1 * num2
        st.success(f"Hasil Perkalian: {result}")
    elif operation == "Pembagian":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Hasil Pembagian: {result}")
        else:
            st.error("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
else:
    st.info("Masukkan angka dan klik tombol 'Hitung' untuk melihat hasil.")
    
# Footer
st.sidebar.write("Project dibuat oleh Mulyana.")
