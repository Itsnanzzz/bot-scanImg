import pytesseract
from PIL import Image
import os

def scan_text(image_path, language='eng'):
    """
    Fungsi untuk memindai teks dari gambar
    :param image_path: Path ke file gambar
    :param language: Bahasa yang digunakan (eng/ind)
    :return: Teks yang terdeteksi
    """
    try:
        # Buka gambar menggunakan PIL
        image = Image.open(image_path)
        
        # Lakukan OCR pada gambar
        text = pytesseract.image_to_string(image, lang=language)
        
        return text
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

def main():
    # Minta input path gambar dari user
    image_path = input("Masukkan path file gambar (contoh: gambar.jpg): ")
    
    # Periksa apakah file ada
    if not os.path.exists(image_path):
        print("File tidak ditemukan!")
        return
    
    # Pilih bahasa
    print("\nPilih bahasa:")
    print("1. Inggris (eng)")
    print("2. Indonesia (ind)")
    choice = input("Pilihan (1/2): ")
    language = 'ind' if choice == '2' else 'eng'
    
    # Lakukan pemindaian
    print("\nMemindai teks...")
    result = scan_text(image_path, language)
    
    # Tampilkan hasil
    print("\nHasil pemindaian:")
    print("-" * 50)
    print(result)
    print("-" * 50)
    
    # Simpan hasil ke file
    output_file = "hasil_scan.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"\nHasil telah disimpan ke file: {output_file}")

if __name__ == "__main__":
    main() 