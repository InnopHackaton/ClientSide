[![OS](https://img.shields.io/badge/platform-linux-blue.svg)](https://www.kernel.org/)
[![](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/download/releases/3.6.0/)
![](https://img.shields.io/docker/automated/vladius25/serverside.svg?colorB=brightgreen)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/InnopHackaton/ClientSide.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/InnopHackaton/ClientSide/context:python)

### Зимний хакатон Иннополиса
# Схема
Клиент связывается с сервером(порт 1338), получает от него публичный
ключ(4096 бит). Шифрует сообщения, отправляет на сервер(порт
1337). Сервер расшифровывает данные и снова шифрует алгоритмом AES,
отправялет вторуму клиенту. Схема рботает в двух  направлениях.

Клиент А - 172.0.0.2

Модем - 172.0.0.2

Сервер - 10.0.5.6

Модем - 172.0.0.2

Клиент А - 172.0.0.1

# Установка
Сборка:

`docker-compose build`

Запуск:

`docker-compose run messager`

# Конфигурирование
Файлы конфигурации находятся в папке configs: для настрок сети, ключей
