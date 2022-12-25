from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description="<h1>API для получения данных о вашем гороскопе c сайта https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx</h1>"\
    "<h2>*Подсказка по знакам зодика на английском*</h2>"\
    "<h3>Aries - Овен, Taurus - Телец, Gemini - Близнецы,\n Cancer - Рак, Leo - Лев, Virgo - Дева,\n Libra - Весы, Scorpio - Скорпион, Sagittarius - Стрелец,\n Capricorn - Козерог, Aquarius - Водолей, Pisces - Рыбы</h3>", 
    license='MIT',
    contact='Гнатюк Анна',
    contact_email='nyusha_gnatyuk@mail.ru',
    phone='89289339086',
    doc='/',
    prefix='/api/v1'
)

from core import routes
