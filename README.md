### Веб сервис для загрузки прошивок на оборудование по ftp ###

Для запуска - склонируйте проект командой git clone https://github.com/ant4p/input_ip_and_upload_file_to_ftp.git  <br/>
Создайте виртуальное окружение.<br/>
Установите в виртуальное окружение файл requirements.txt командой pip install -r requirements.txt<br/>
Файл .env_example замените на .env c вашими данными: <br/>
SECRET_KEY - ваш секретный ключ от django<br/>
PORT - порт для подключения к FTP серверу<br/>
USER - пользователь с правами доступа для записи в каталог "/"<br/>
(ОБЯЗАТЕЛЬНО! Проверяйте права доступа пользователя для записи в корневой каталог, т.к. по умолчанию их нет)<br/>
USER_PASSWORD - пароль от пользователя<br/>
Для минимально рабочего функционала - этого будет достаточно.<br/>
В корневой папке проекта осуществите миграции командой python manage.py migrate<br/>
Запустите проект на локальном сервере командой python manage.py runserver<br/>
При переходе на http://127.0.0.1:8000 будет доступна страница:<br/>
<br/>
<p align="center">
 <img width=auto, height=1000 src="images/main_page.png" alt="output"/>
</p>
<br/>
Введите данные IP-адреса устройства, и загрузите файл конфигурации<br/>
(в данном варианте это .txt файл)<br/>
При правильном вводе данных IP-адреса, а так-же размера и формата загружаемого файла -  вы получите:
<br/>
<p align="center">
 <img width=auto, height=1000 src="images/main_page_successfull.png" alt="output"/>
</p>
При вводе неправильных данных - форма провалидирует данные и выдаст всплывающие подсказки.<br/>
<br/>
Для проверки в корневом каталоге вашего FTP cервера - появится загружаемый файл.<br/>
<p align="center">
 <img width=auto, height=1000 src="images/root_directory.png" alt="output"/>
</p>
<br/>
<p align="center">
 <img width=auto, height=1000 src="images/root_directory_with_file.png" alt="output"/>
</p>
<br/>
Веб сервис подготовлен для деплоя на сервер с помощью Docker и Docker compose.<br/>
Для этого понадобится VPS c установленными Docker и Docker compose, и минимально настроенными политиками безопасности.<br/>
Для запуска - склонируйте проект командой git clone https://github.com/ant4p/input_ip_and_upload_file_to_ftp.git<br/>
Файл .env_example замените на .env c вашими данными: <br/>
SECRET_KEY - ваш секретный ключ от django<br/>
PORT - порт для подключения к FTP серверу<br/>
USER - пользователь с правами доступа для записи в каталог "/"<br/>
USER_PASSWORD - пароль от пользователя<br/>:
POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD - данные для БД PostgreSQL<br/>
ALLOWED_HOST, SCRF_SUBDOMAIN=*. - доменное имя<br/>

Перейдите в папку с проектом и запустите docker-compose.yml файл командой: docker compose up <br/>
После того, как проект сбилдится и запустится - <br/>
перейдите по адресу доменного имени, он будет доступен по протоколу https<br/>

Для веб сервиса использованы:<br/>
Локальный запуск:<br/>
python3.12 - ЯП<br/>
pip -пакетный менеджер<br/>
python venv - в качестве виртуального окружения<br/>
Django 5.2.5 - основа<br/>
python-dotenv переменные окружения .env<br/>
ftplib - для взаимодействия с FTP<br/>
sqlite3 - в качестве стандартной БД для django<br/>
<br/>
На сервере + :<br/>
Docker compose - для финальной сборки <br/>
Docker - для сборки образов <br/>
PostgreSQL - в качестве БД <br/>
NGINX - в качестве веб сервера <br/>
acme-companion - для получения бесплатных ssl сертификатов <br/>

