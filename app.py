import requese, random
from bs4 import beautyfulsoup
from flask import flask, request, abort
from linebot import (
  lineBotApi,Webhookhandler
)
from linebot.execeptions import (
  InvalidSignatureError
)
from linebot.models import *

app = Flask(_name_)
line_bot_api= LineBotApi('9UqcHjiCzjEpbxBa//hlWWFvY79FC2PVc9CfRlhaOOXSozfPWpfsK4rSFpF/lwNwgsoS7qnKrk4TKTZes9CFdTFxAAUztx6VFZ8o3mPUlvJkVHrE2dsVoaN+UOSIU7A58/zbdp5TtFQpJWWGuSnyRAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c9e4610cf78163336e6cc81319358d5d')
@app.route("/callback", methods=['POST'])

  
  def ptt_random_pic():

    target_url = 'https://www.ptt.cc/bbs/Beauty/index.html'
    res = requests.get(target_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    pic_urls = []
    while (len(pic_urls) < 1):
        for data in soup.select('.r-ent'):
            pushes = data.select_one('.nrec').text
            if pushes == '爆' or (pushes != '' and 'X' not in pushes and int(pushes) > 50):
                title = data.find('a', href=True)
                heading = title.text
                link = 'https://www.ptt.cc' + title['href']
                if '公告' in heading:
                    continue
                res2 = requests.get(link)
                soup2 = BeautifulSoup(res2.text, 'html.parser')
                for data2 in soup2.select_one('#main-content').find_all('a', href=True):
                    if 'https://i.imgur.com' in data2['href']:
                       pic_urls.append(data2['href'])
                break
        last_page_url = 'https://www.ptt.cc' + soup.select('.btn.wide')[1]['href']
        res = requests.get(last_page_url)
        soup = BeautifulSoup(res.text, 'html.parser')

    return random.choice(pic_urls)
  @handler.add(MessageEvent, message=TextMessage)

def handle_message(event):

    if event.message.text == '插':
        content = apple_news()
        content = ptt_random_pic()
        
        image_message = ImageSendMessage(
            original_content_url=content,
            preview_image_url=content
        )
     line_bot_api.reply_message(
            event.reply_token,
            image_message
        )
        return
        if __name__ == "__main__":

    app.run()
