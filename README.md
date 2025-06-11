# Program Scanner Teks dan QR Code Python

Program ini dapat memindai teks dan QR Code dari gambar menggunakan teknologi OCR (Optical Character Recognition) dan tersedia dalam dua versi:
1. Versi CLI (Command Line Interface)
2. Versi Bot Telegram

## Persyaratan

1. Python 3.6 atau lebih baru
2. Tesseract OCR harus terinstal di sistem Anda
   - Untuk Windows: Download dan instal dari https://github.com/UB-Mannheim/tesseract/wiki
   - Untuk Linux: `sudo apt-get install tesseract-ocr`
   - Untuk macOS: `brew install tesseract`

3. ZBar (untuk fitur QR Code)
   - Untuk Windows: Download dan instal dari https://sourceforge.net/projects/zbar/files/zbar/0.10/
   - Untuk Linux: `sudo apt-get install libzbar0`
   - Untuk macOS: `brew install zbar`

## Instalasi

1. Clone repositori ini
   ```
   git clone https://github.com/Itsnanzzz/bot-scanImg
   ```
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
   - `/qrcode` - Memulai mode pemindaian QR Code
   - Kirim gambar langsung - Bot akan memproses teks dalam gambar
   - Kirim gambar setelah `/qrcode` - Bot akan memproses QR Code dalam gambar

## Fitur Bot Telegram

### Scan Teks
- Kirim gambar langsung ke bot
- Bot akan mendeteksi dan mengekstrak teks dari gambar
- Hasil akan dikirim dalam format teks

### Scan QR Code
1. Kirim command `/qrcode`
2. Bot akan meminta Anda mengirim gambar
3. Kirim gambar yang berisi QR Code
4. Bot akan mengirimkan hasil yang mencakup:
   - Tipe QR Code
   - Data yang terkandung dalam QR Code

## Catatan

- Program mendukung format gambar umum seperti JPG, PNG, BMP
- Untuk hasil terbaik, gunakan gambar dengan teks yang jelas dan kontras yang baik
- Program menggunakan bahasa Inggris sebagai default untuk pemindaian
- Untuk menggunakan bahasa Indonesia, pastikan file `ind.traineddata` sudah terinstal di folder Tesseract
- Untuk hasil QR Code terbaik:
  - Pastikan QR Code terlihat jelas
  - Hindari gambar yang blur
  - Pastikan pencahayaan cukup
  - QR Code sebaiknya tidak terpotong
  - Hindari pantulan cahaya pada QR Code 