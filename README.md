# CorporoSano
# Language Filter and Data Sanitizer for Non-English Code-Switched Text
[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

## English
This repository contains a Python script that processes text files in a folder, removes English-language snippets from code-switched text, and retains non-English text and short English phrases (1-3 words). The script also creates a backup of the original text files in a subfolder.

### (Code-switching: Linguistic term for mixing languages when speaking, for example: "Apa kabar sih darling, what are you doing here?")

### Features
- Language identification and filtering: The script identifies and removes English-language snippets from code-switched text.
- Data sanitation: The script removes URLs, phone numbers, and meaningless words with mixed letters and numbers (e.g., "Hk3j4") while keeping words like GPT4 and DEFCON4.

### Usage
1. Clone this repository to your local machine.
2. Place the text files you want to process in the `path_to_text_files` folder.
3. Run the `corporosano.py` script.

The script will process each text file, create a backup in the `backup` subfolder, and remove English-language snippets from the original text files. The modified files will be saved in the original folder.

### Example
```python
folder_path = './path_to_text_files'
process_text_files(folder_path)
```
### Requirements
- Python 3
- langid.py library

To install the langid.py library, use the following command:
```
pip install langid
```
### Notes
- The script uses the `langid.py` library to identify the language of each sentence in the text files.
- The script removes English-language snippets, except for short English phrases (1-3 words).
- The script creates a backup of the original text files in the `backup` subfolder.
- Please test the script on a sample dataset before using it on your actual data to ensure that it works as expected.


## Bahasa Indonesia
Repositori ini berisi skrip Python yang memproses file teks dalam folder, menghapus potongan teks berbahasa Inggris dari teks campuran (code-switched), dan mempertahankan teks non-Bahasa Inggris dan frasa Bahasa Inggris pendek (1-3 kata). Skrip ini juga membuat cadangan file teks asli dalam subfolder.

### (Code-switching: Istilah linguistik untuk bahasa campur sari seperti: "Apa kabar sih darling, what are you doing here?")

### Fitur
- Identifikasi dan penyaringan bahasa: Skrip mengidentifikasi dan menghapus potongan teks berbahasa Inggris dari teks campuran.
- Sanitasi data: Skrip menghapus URL, nomor telepon, dan kata-kata tidak berarti dengan campuran huruf dan angka (mis., "Hk3j4") dan tidak menghapus kata-kata seperti GPT2 dan TV3.

### Cara Penggunaan
1. Kloning repositori ini ke komputer lokal Anda.
2. Letakkan file teks yang ingin diproses di folder `path_to_text_files`.
3. Jalankan skrip `corporosano.py`.

Skrip ini akan memproses setiap file teks, membuat cadangan di subfolder `backup`, dan menghapus potongan teks berbahasa Inggris dari file teks asli. File yang telah dimodifikasi akan disimpan di folder asli.

### Catatan
- Skrip ini menggunakan library `langid.py` untuk mengidentifikasi bahasa dari setiap kalimat dalam file teks.
- Skrip ini menghapus potongan teks berbahasa Inggris, kecuali frasa Bahasa Inggris pendek (1-3 kata).
- Skrip ini membuat cadangan file teks asli di subfolder `backup`.
- Harap uji skrip pada data lain yang Anda punya sebagai sampel sebelum menggunakannya pada data Anda yang sebenarnya untuk memastikan bahwa skrip berfungsi sesuai yang diharapkan.

