import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pytesseract
from PIL import Image
import io
import os

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

# Handler untuk command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Saya adalah bot OCR.\n"
        "Kirimkan gambar yang berisi teks, dan saya akan mencoba membacanya untuk Anda."
    )

# Handler untuk command /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Cara menggunakan bot:\n"
        "1. Kirim gambar yang berisi teks\n"
        "2. Tunggu sebentar\n"
        "3. Bot akan mengirimkan hasil pembacaan teks\n\n"
        "Tips: Gunakan gambar dengan teks yang jelas dan kontras yang baik untuk hasil terbaik."
    )

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
        
        # Proses gambar
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
    TOKEN = "7419253164:AAFXQySdqrQrp5bgBpZ1_6Mwod4R6hg3LdA"
    
    # Buat aplikasi
    application = Application.builder().token(TOKEN).build()

    # Tambahkan handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))

    # Jalankan bot
    print("Bot sedang berjalan...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 