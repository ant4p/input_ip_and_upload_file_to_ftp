### Веб сервис для загрузки прошивок на оборудование по ftp ###

Для запуска - склонируйте проект командой git clone   <br/>
Создайте виртуальное окружение.<br/>
Установите в виртуальное окружение файл requirements.txt командой pip install -r requirements.txt<br/>
Файл .env_example замените на .env c вашими данными: <br/>
SECRET_KEY - ваш секретный ключ от django<br/>
PORT - порт для подключения к FTP серверу<br/>
USER - пользователь с правами доступа для записи в каталог "/"<br/>
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
Для проверки в корневом каталоге - появится загружаемый файл.<br/>
<p align="center">
 <img width=auto, height=1000 src="images/root_directory.png" alt="output"/>
</p>
<br/>
<p align="center">
 <img width=auto, height=1000 src="images/root_directory_with_file.png" alt="output"/>
</p>