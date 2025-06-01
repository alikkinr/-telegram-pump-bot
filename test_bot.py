from flask import Flask, request
import requests

TOKEN = '8154789650:AAGiLnZfFm_qS5X6k9LoiMK93t18mZ436tg'
CHAT_ID = '289615947'  # آی‌دی عددی تو
API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is live!'

@app.route('/send_test', methods=['GET'])
def send_test():
    message = (
        "🚨 [تست اتصال موفق] \n"
        "🪙 توکن فرضی: $TESTINU \n"
        "📈 رشد: +222%\n"
        "🐋 نهنگ وارد شد!\n"
        "🔗 لینک خرید: https://jup.ag/swap/SOL-TESTINU"
    )
    requests.post(API_URL, data={'chat_id': CHAT_ID, 'text': message})
    return 'پیام فرستاده شد!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
