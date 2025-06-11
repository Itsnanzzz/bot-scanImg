# Program Scanner Teks Python

Program ini dapat memindai teks dari gambar menggunakan teknologi OCR (Optical Character Recognition) dan tersedia dalam dua versi:
1. Versi CLI (Command Line Interface)
2. Versi Bot Telegram

## Persyaratan

1. Python 3.6 atau lebih baru
2. Tesseract OCR harus terinstal di sistem Anda
   - Untuk Windows: Download dan instal dari https://github.com/UB-Mannheim/tesseract/wiki
   - Untuk Linux: `sudo apt-get install tesseract-ocr`
   - Untuk macOS: `brew install tesseract`

## Instalasi

1. Clone repositori ini
2. Instal dependensi yang diperlukan:
   ```
   pip install -r requirements.txt
   ```

## Penggunaan

### Versi CLI
1. Jalankan program:
   ```
   python scanner.py
   ```
2. Masukkan path file gambar yang ingin dipindai
3. Program akan menampilkan hasil pemindaian dan menyimpannya ke file `hasil_scan.txt`

### Versi Bot Telegram
1. Pastikan Anda sudah memiliki bot Telegram (dari @BotFather)
2. Token bot sudah dikonfigurasi di `telegram_bot.py`
3. Jalankan bot:
   ```
   python telegram_bot.py
   ```
4. Gunakan bot di Telegram:
   - `/start` - Memulai bot dan melihat pesan selamat datang
   - `/help` - Melihat bantuan penggunaan
   - Kirim gambar - Bot akan memproses gambar dan mengirimkan hasil OCR

## Catatan

- Program mendukung format gambar umum seperti JPG, PNG, BMP
- Untuk hasil terbaik, gunakan gambar dengan teks yang jelas dan kontras yang baik
- Program menggunakan bahasa Inggris sebagai default untuk pemindaian
- Untuk menggunakan bahasa Indonesia, pastikan file `ind.traineddata` sudah terinstal di folder Tesseract 