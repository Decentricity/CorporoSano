import os
import shutil
import langid
import re

def sanitize_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove phone numbers (assuming common formats)
    text = re.sub(r'\+?\d{1,4}[-.\s]?\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}', '', text)
    
    # Tokenize the text into words
    words = text.split()
    
    # Remove words with a mix of letters and numbers, but keep words with characters followed by 1-2 numbers
    words = [word for word in words if not re.match(r'^.*[a-zA-Z]+.*\d+.*[a-zA-Z]+.*$', word)]
    
    # Join the words back into a single text
    result = ' '.join(words)
    return result

def remove_english_text(text):
    # Split the text into sentences or phrases
    sentences = text.split('\n')
    
    # Identify the language of each sentence and keep only non-English sentences
    non_english_sentences = [sentence for sentence in sentences if langid.classify(sentence)[0] != 'en']
    
    # Join the non-English sentences back into a single text
    result = '\n'.join(non_english_sentences)
    return result

def process_text_files(folder_path):
    # Define the path to the backup subfolder
    backup_folder = os.path.join(folder_path, 'backup')
    
    # Create the backup subfolder if it doesn't exist
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            
            # Backup the original file
            shutil.copy(file_path, backup_folder)
            
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Sanitize the text
            sanitized_content = sanitize_text(content)
            
            # Remove English-language snippets
            modified_content = remove_english_text(sanitized_content)
            
            # Write the modified content back to the original file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)

# Example usage
folder_path = './path_to_text_files'
process_text_files(folder_path)
