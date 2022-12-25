# Flask_laba_7

API позволит распарсить сайт с гороскопами 
Можно узнать гороскоп на определённый день\неделю\месяц

Что нужно сделать что бы сайт заработал

-Создать виртуальную среду

     $ python -m venv env
  
-Чтобы активировать виртуальную среду с именем env, используйте следующие команды:

    в Windows — env\Scripts\activate.bat
    в Linux и MacOS — source env/bin/activate
    deactivate - деакцивация
 
 -Установите следующие библиотеки

    $ pip install requests Библиотека requests позволяет очень легко отправлять запросы.
    $ pip install bs4 Beautiful Soup (bs4) – это библиотека Python для извлечения данных из файлов HTML и XML.
    $ pip install flask Он помогает создавать масштабируемые и безопасные веб-приложения.
    $ pip install flask-restx Позволяет создавать API с помощью документации Swagger.
    $ pip install python-decouple Мы также будем использовать переменные среды в этом проекте.
 
-Запустить файл который поможет нам запустить сервер Flask

    $ python main.py   
