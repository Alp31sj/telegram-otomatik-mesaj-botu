import schedule
import time
from pyrogram import Client

api_id = #my.telegram.org'tan aldıgınız api_id
api_hash = 'my.telegram.org'tan aldıgınız api_hash'
session_string = 'getsessionstring ten aldıgınız kod'

app = Client(session_string, api_id, api_hash)

n = 0

def job():
    global n
    app.send_message("grup", "mesaj")
    n += 1


# schedule.every().day.at("10:30").do(job)
schedule.every(20).seconds.do(job)
# schedule.every(30).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

with app:
    while True:
        schedule.run_pending()
        time.sleep(1)
        if n == 1:
            app.send_message(
                "me", f"istenilen kadar mesaj gonderildi")
            break  
# with app:
#    n = 0
#    while n < 99999:
#        app.send_message("", f"T")
#        time.sleep(30)
#         n += 1

# app.run()
