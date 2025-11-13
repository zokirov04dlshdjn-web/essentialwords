import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

pdf_files = {
    "Essential 1": "https://drive.google.com/uc?export=download&id=PDF_ID_1",
    "Essential 2": "https://drive.google.com/uc?export=download&id=PDF_ID_2",
    "Essential 3": "https://drive.google.com/uc?export=download&id=PDF_ID_3",
    "Essential 4": "https://drive.google.com/uc?export=download&id=PDF_ID_4",
    "Essential 5": "https://drive.google.com/uc?export=download&id=PDF_ID_5",
    "Essential 6": "https://drive.google.com/uc?export=download&id=PDF_ID_6"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! 👋 Men Essential Words botman.\n"
        "So'zlarni o‘rganish va PDFlarni yuklash uchun /menu ni bosing."
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📝 Quiz boshlash", "📖 PDF yuklash"],
        ["🏆 Musobaqalar", "ℹ️ Info"]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bo‘limni tanlang:", reply_markup=markup)

async def button_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📝 Quiz boshlash":
        await update.message.reply_text("Quiz bo‘limi tez orada ishga tushadi! 😊")

    elif text == "📖 PDF yuklash":
        keyboard = [
            ["Essential 1", "Essential 2", "Essential 3"],
            ["Essential 4", "Essential 5", "Essential 6"],
            ["⬅️ Orqaga"]
        ]
        markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("PDF kitobni tanlang:", reply_markup=markup)

    elif text == "🏆 Musobaqalar":
        await update.message.reply_text("Musobaqalar bo‘limi tez orada ishga tushadi! 🏁")

    elif text == "ℹ️ Info":
        await update.message.reply_text("Bu bot Essential Words kitoblari asosida so‘zlarni o‘rganish uchun yaratilgan.")

    elif text in pdf_files:
        pdf_url = pdf_files[text]
        await update.message.reply_document(chat_id=update.message.chat_id, document=pdf_url)
        await menu(update, context)

    elif text == "⬅️ Orqaga":
        await menu(update, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_choice))
    print("Bot is running...")
    app.run_polling()
