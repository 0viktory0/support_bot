# Бот службы поддержки

Бот для службы поддержки в Telegram и VK.<br>
Создание диалогов происходит через сервис [Dialogflow](https://dialogflow.cloud.google.com/)


## Установка
- Предварительно должен быть установлен Python3.
- Для установки зависимостей, используйте команду `pip` (или `pip3`, если 
есть конфликт с `Python2`)

```
pip install -r requirements.txt
```

- Создайте проект в [GoogleCloud](https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.102882952.945628098.1664273348-1333030587.1663324445) и получите его id
- Зайдите под тем же гугл-аккаунтом в [Dialogflow](https://dialogflow.cloud.google.com/) и создайте агента, выбрав предварительно созданный проект
- Подключите API вашего проекта по [ссылке](https://console.cloud.google.com/flows/enableapi?apiid=dialogflow.googleapis.com&_ga=2.235976969.945628098.1664273348-1333030587.1663324445)
- Скачайте и установите [GCloudCLI](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe)
- В командной строке введите `gcloud auth application-default login`
- Для работы Telegram бота получите его токен у @BotFather
- Для работы VK бота создайте группу и получите ключ API для работы с сообщениями сообщества.


- В папке со скриптом необходимо создать файл `.env` и записать в него настройки в виде:
```
DIALOGFLOW_PROJECT_ID=id проекта Dialogflow
TG_BOT_TOKEN=токен Telegram бота
VK_API_TOKEN=токен API группы VK
GOOGLE_APPLICATION_CREDENTIALS=путь до файла json с секретным ключом
```
 

## Запуск кода

Telegram бот
    
```
python3 telegram_bot.py 
``` 


VK бот
    
```
python3 vk_bot.py 
``` 


## Тренировка бота
Чтобы научить бота обрабатывать запросы пользователя, нужно добавить в него Intents (цели).<br>
Создайте .json файл (вместо `questions.json`) в каталоге программы в следующем формате:

```
{
    "Цель": {
        "questions": [
            "Вопрос(ы)", 
        ],
        "answer": "Ответ"
    },
}

```

Запускайте скрипт тренировки бота
```
python3 dialog_flow.py
``` 
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).