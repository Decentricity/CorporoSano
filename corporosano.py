import os
import shutil
import langid

def remove_english_text(text):
    # Split the text into sentences or phrases
    # Memisahkan teks menjadi kalimat atau frasa
    sentences = text.split('\n')
    
    # Identify the language of each sentence and keep only non-English sentences
    # or short English phrases (1-3 words)
    # Mengidentifikasi bahasa dari setiap kalimat dan menyimpan hanya kalimat non-Bahasa Inggris
    # atau frasa Bahasa Inggris pendek (1-3 kata)
    non_english_sentences = []
    for sentence in sentences:
        lang, _ = langid.classify(sentence)
        num_words = len(sentence.split())
        if lang != 'en' or (lang == 'en' and num_words <= 3):
            non_english_sentences.append(sentence)
    
    # Join the non-English sentences back into a single text
    # Menggabungkan kembali kalimat non-Bahasa Inggris menjadi satu teks
    result = '\n'.join(non_english_sentences)
    return result

def process_text_files(folder_path):
    # Define the path to the backup subfolder
    # Menentukan jalur ke subfolder cadangan
    backup_folder = os.path.join(folder_path, 'backup')
    
    # Create the backup subfolder if it doesn't exist
    # Membuat subfolder cadangan jika belum ada
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    
    # Iterate over all files in the folder
    # Melakukan iterasi pada semua file dalam folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            # Construct the full file path
            # Membuat jalur file lengkap
            file_path = os.path.join(folder_path, filename)
            
            # Backup the original file
            # Mencadangkan file asli
            shutil.copy(file_path, backup_folder)
            
            # Read the content of the file
            # Membaca isi file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Remove English-language snippets, except for short phrases
            # Menghapus potongan teks berbahasa Inggris, kecuali frasa pendek
            modified_content = remove_english_text(content)
            
            # Write the modified content back to the original file
            # Menulis kembali konten yang telah dimodifikasi ke file asli
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)

# Example usage
# Contoh penggunaan
folder_path = './path_to_text_files'
process_text_files(folder_path)
