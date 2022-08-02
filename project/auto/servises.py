import os
from dotenv import load_dotenv
import requests
from project.settings import MEDIA_ROOT


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


def send_message(automobile, chat_id):
    model = automobile.model
    brand = automobile.brand
    photo_path = os.path.join(MEDIA_ROOT, str(automobile.photo))
    photo = open(str(photo_path), 'rb')
    payload = {
        'chat_id': chat_id,
        'caption': f'{brand} - {model}',
        'parse_mode': 'html'
    }
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto'
    resp = requests.post(url, data=payload, files={'photo': photo})
    return resp.json()
