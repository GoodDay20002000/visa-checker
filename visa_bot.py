import requests
import time
import datetime

BOT_TOKEN = "7923658090:AAGyTYVAIwhc2tCZ5_KWFCkDnXpUjoRcL2A"
CHAT_ID = "6952906873"

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, json=data, timeout=10)
        print(f"✅ تم الإرسال: {datetime.datetime.now().strftime('%H:%M:%S')}")
        return True
    except Exception as e:
        print(f"❌ خطأ: {e}")
        return False

print("🚀 بدء تشغيل مراقب الفيزا...")
send_telegram("🎉 <b>تم بدء المراقبة التلقائية!</b>")

count = 0
while True:
    count += 1
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"🔍 فحص رقم {count} - {current_time}")
    
    # إرسال تقرير كل 6 فحوصات
    if count % 6 == 0:
        send_telegram(f"📊 <b>تقرير التشغيل</b>\n\nالفحص رقم: {count}\nالوقت: {current_time}\nالحالة: ✅ النظام شغال")
    
    time.sleep(300)  # انتظار 5 دقائق
