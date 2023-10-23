# Fungsi untuk melakukan enkripsi Caesar Cipher
def custom_caesar_encrypt(plaintext, key):
    result = ""
    
    for char in plaintext:
        if char.isalpha():
            # Menentukan offset ASCII sesuai dengan huruf kecil atau besar
            ascii_offset = ord('a') if char.islower() else ord('A')
            # Menggeser karakter sesuai dengan kunci
            shifted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char  # Menambahkan karakter selain huruf
    
    return result

# Fungsi untuk melakukan enkripsi Vigenere Cipher
def vigenere_encrypt(plaintext, keyword):
    result = ""
    keyword = keyword.lower()
    keyword_length = len(keyword)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            # Menentukan offset ASCII sesuai dengan huruf kecil atau besar
            ascii_offset = ord('a') if char.islower() else ord('A')
            # Mendapatkan indeks kunci untuk karakter saat ini
            key_index = ord(keyword[i % keyword_length]) - ord('a')
            # Menggeser karakter sesuai dengan kunci
            shifted_char = chr((ord(char) - ascii_offset + key_index) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char  # Menambahkan karakter selain huruf
    
    return result

# Fungsi untuk menghasilkan dictionary shift values dari kunci
def generate_shift_key(key):
    key = key.lower()
    shift_values = {}
    for i, char in enumerate(key):
        # Menghitung nilai geser berdasarkan urutan huruf di kunci
        shift = ord(char) - ord('a')
        shift_values[chr(ord('a') + i)] = shift
    
    return shift_values

# Teks yang akan dienkripsi
plaintext = "Success is not final, failure is not fatal, it is the courage to continue that counts"

# Kunci Caesar Cipher
caesar_key = 3

# Kunci Vigenere Cipher
vigenere_key = "Deswinta"

# Enkripsi dengan Caesar Cipher
caesar_ciphertext = custom_caesar_encrypt(plaintext, caesar_key)

# Enkripsi dengan Vigenere Cipher setelah Caesar Cipher
vigenere_ciphertext = vigenere_encrypt(caesar_ciphertext, vigenere_key)

# Menampilkan hasil enkripsi
print("Plaintext:", plaintext)
print("Caesar Ciphertext:", caesar_ciphertext)
print("Vigenere Ciphertext:", vigenere_ciphertext)
