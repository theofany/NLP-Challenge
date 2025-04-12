import re
from langdetect import detect
from collections import Counter
import streamlit as st

# Judul aplikasi
st.title("Auto Tokenization and Language Detection")

# Input teks dari pengguna
inputan_kata = st.text_area("Input Text:", "")

# Proses jika tombol ditekan
if st.button("Process"):
    if inputan_kata.strip():
        # Deteksi bahasa
        try:
            bahasa = detect(inputan_kata)
            if bahasa == 'en':
                st.write("Language: Inggris")
            elif bahasa == 'id':
                st.write("Language: Indonesia")
            elif bahasa == 'fr':
                st.write("Language: Prancis")
            elif bahasa == 'es':
                st.write("Language: Spanyol")
            elif bahasa == 'de':
                st.write("Language: Jerman")
            elif bahasa == 'ja':
                st.write("Language: Jepang")
            elif bahasa == 'ko':
                st.write("Language: Korea")
            elif bahasa == 'zh':
                st.write("Language: Mandarin")
            elif bahasa == 'ru':
                st.write("Language: Rusia")
            elif bahasa == 'pt':
                st.write("Language: Portugis")
            else:
                st.write("No Language Detectedd.")
        except Exception as e:
            st.error(f"Error: {e}")
            bahasa = None
        # Normalisasi teks
        inputan_kata = inputan_kata.lower()
        inputan_kata = re.sub(r'[^\w\s]', '', inputan_kata)
        st.write("Text after Normalization:", inputan_kata)

        # Tokenisasi otomatis
        token_kata = inputan_kata.split()
        st.write("Tokenization:", token_kata)

        # Hitung frekuensi kata
        frekuensi_kata = Counter(token_kata)
        st.subheader("Word Frequency:")
        for kata, frekuensi in frekuensi_kata.items():
            st.write(f"{kata}: {frekuensi}")
    else:
        st.warning("Input Text First!")