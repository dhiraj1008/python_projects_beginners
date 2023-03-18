#sending goodmorning msg using python .
# use schedule and textbelt (request) module
# textbelt is demo key which sends the msg once a day.if we want to send more than need to pay..!
import requests
from credentials import mobile_number
import schedule
import time
def send_meassage():
    # to send the required information to the specified url.
    resp = requests.post('https://textbelt.com/text',{
                         'phone':mobile_number,
                         'message':'Hey,good morning',
                         'key':'textbelt'
                         }
                         )
    print(resp.json())

#schedule.every().day.at('14:22').do(send_meassage)
schedule.every(10).seconds.do(send_meassage)

while True:
    schedule.run_pending()
    time.sleep(1)