import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pytesseract
from PIL import Image
import io
import os
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Konfigurasi logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Fungsi untuk memproses gambar
async def process_image(image_data):
    try:
        # Buka gambar dari bytes
        image = Image.open(io.BytesIO(image_data))
        
        # Lakukan OCR
        text = pytesseract.image_to_string(image, lang='eng')
        
        return text if text.strip() else "Tidak ada teks yang terdeteksi dalam gambar."
    except Exception as e:
        return f"Terjadi kesalahan saat memproses gambar: {str(e)}"

# Fungsi untuk memindai QR Code
async def scan_qr_code(image_data):
    try:
        # Konversi bytes ke numpy array
        nparr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Deteksi QR Code
        decoded_objects = decode(img)
        
        if not decoded_objects:
            return "Tidak ada QR Code yang terdeteksi dalam gambar."
        
        # Kumpulkan semua hasil
        results = []
        for obj in decoded_objects:
            # Decode bytes ke string
            data = obj.data.decode('utf-8')
            # Tambahkan tipe QR Code
            qr_type = obj.type
            results.append(f"Tipe: {qr_type}\nData: {data}")
        
        return "\n\n".join(results)
    except Exception as e:
        return f"Terjadi kesalahan saat memindai QR Code: {str(e)}"

# Handler untuk command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Saya adalah bot OCR dan QR Code Scanner.\n"
        "Fitur yang tersedia:\n"
        "1. Scan teks dari gambar (kirim gambar langsung)\n"
        "2. Scan QR Code (/qrcode)\n\n"
        "Gunakan /help untuk bantuan lebih lanjut."
    )

# Handler untuk command /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Cara menggunakan bot:\n\n"
        "1. Scan Teks:\n"
        "   - Langsung kirim gambar yang berisi teks\n"
        "   - Bot akan mengirimkan hasil pembacaan teks\n\n"
        "2. Scan QR Code:\n"
        "   - Gunakan command /qrcode\n"
        "   - Kirim gambar yang berisi QR Code\n"
        "   - Bot akan mengirimkan hasil pembacaan QR Code\n\n"
        "Tips:\n"
        "- Gunakan gambar dengan kualitas baik\n"
        "- Pastikan teks/QR Code terlihat jelas\n"
        "- Hindari gambar yang blur atau gelap"
    )

# Handler untuk command /qrcode
async def qrcode_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Silakan kirim gambar yang berisi QR Code.\n"
        "Bot akan mencoba memindai QR Code dalam gambar tersebut."
    )
    # Set state untuk menunggu gambar QR Code
    context.user_data['waiting_for_qr'] = True

# Handler untuk gambar
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Kirim pesan "memproses"
    processing_message = await update.message.reply_text("Memproses gambar ⌛...")
    
    try:
        # Dapatkan file foto terbesar
        photo = update.message.photo[-1]
        
        # Download foto
        photo_file = await context.bot.get_file(photo.file_id)
        photo_bytes = await photo_file.download_as_bytearray()
        
        # Cek apakah user sedang menunggu QR Code
        if context.user_data.get('waiting_for_qr'):
            # Scan QR Code
            result = await scan_qr_code(photo_bytes)
            context.user_data['waiting_for_qr'] = False
        else:
            # Scan teks
            result = await process_image(photo_bytes)
        
        # Kirim hasil
        await update.message.reply_text(f"Hasil pemindaian:\n\n{result}")
        
    except Exception as e:
        await update.message.reply_text(f"Maaf, terjadi kesalahan: {str(e)}")
    
    finally:
        # Hapus pesan "memproses"
        await processing_message.delete()

def main():
    # Ganti TOKEN dengan token bot Anda
    TOKEN = "<TOKEN BOT TELEGRAM>"
    
    # Buat aplikasi
    application = Application.builder().token(TOKEN).build()

    # Tambahkan handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("qrcode", qrcode_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))

    # Jalankan bot
    print("Bot sedang berjalan...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 