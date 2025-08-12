import ftplib
import os
from dotenv import load_dotenv

load_dotenv()

port = int(os.getenv("PORT", '21'))


def download_to_ftp(host, username, password, file):
    ftp = None
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        print(f"Подключение к IP-адресу: {host} - прошло успешно.")
        ftp.cwd("/")
        ftp.set_pasv(True)
        remote_filename = file.name
        file.seek(0)
        ftp.storbinary(f"STOR {remote_filename}", file)
        return True, f"Файл {remote_filename} успешно загружен в директорию / на {host}"
    except Exception as e:
        return False, f"Ошибка загрузки: {str(e)}"
    finally:
        if ftp:
            try:
                ftp.quit()
                print("Соединение с FTP-сервером закрыто.")
            except:
                pass
