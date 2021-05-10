<h1 align="center">Comm-Bot-Vk</h1>

<p align="center">
<a href="https://github.com/blackcatprog/folder_icons/blob/main/LICENSE"><img alt="LICENSE" src="https://img.shields.io/github/license/tjackenpacken/taskbar-groups?style=for-the-badge" height="20"/></a> 
</p>

## Инструкция для Windows

1) Скачиваем архив с программой:

2) Распаковываем

3) Запускаем comm-bot-win.exe из папки Windows

4) Вводим необходимые данные (Инструкции по получению токена и id поста и пользователя ниже, они одинаковые для Android и Windows) и ожидаем окончания накрутки

## Инструкция для Android

1) Скачиваем архив с программой:

![1](img/1.png)
![2](img/2.png)
![3](img/3.png)
![4](img/4.png)

1) [Скачиваем Termux](https://play.google.com/store/apps/details?id=com.termux "Скачать Termux")

2) Обновляем все доступные пакеты:

```
pkg update
pkg upgrade
```

3) Устанавливаем python:

```
pkg install python
```

3) Даём доступ к внутренней памяти:

```
termux-setup-storage
```

4) Переходим в место, куда вы распаковали архив с программой:

```
cd storage
cd shared
cd Android (если вы распаковали в корневую папку)
```

5) Устанавливаем всё необходимое:

```
pip install -r requirements.txt
```

5) [Получаем токен](https://vkhost.github.io "Получить токен")<br>Выберите Vk Admin и скопируйте часть адресной строки от access_token= до &expires_in

6) Получаем id пользователя и id поста<br>Для этого скопируйте ссылку на пост (id пользователя от wall до _ , а id поста - всё после _

7) Запускаем скрипт:

```
python comm-bot-vk.py
```

8) Вводим все необходимые данные и ждём окончания накрутки.

## Запуск из Source

### Для Windows

1) Скачиваем архив с программой (скриншоты выше)

2) Распаковываем

3) [Устанавливаем Python с официального сайта](https://python.org "Установить Python") (если у вас не установлен)

4) Запускаем консоль сочетанием клавиш Win+R, вводим cmd и нажимаем Enter

5) Переходим в папку с программой (нужно перейти туда, куда вы распаковали архив и открыть папку Source)<br>Ниже приведён пример с папкой на рабочем столе)

```
cd Desktop
cd Source
```

6)  Устанавливаем всё необходимое^

```
pip install -r requirements.txt
```

7) Открываем файл cfg.ini

8) Вписываем всё необходимое (Инструкции по получению токена и id поста и пользователя выше, они одинаковые для Android и Windows)

9) В консоли вводим python comm-bot-vk.py, выбираем сколько нужно комментариев и ожидаем окончания накрутки

###  Для Android

1) 
