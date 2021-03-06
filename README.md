<p align="center"><img src="img/7.png" width=120></p>
<h1 align="center">Comm-Bot-Vk</h1>

<p align="center">
<a href="https://github.com/blackcatprog/comm-bot-vk/releases"><img src="https://img.shields.io/github/v/release/blackcatprog/comm-bot-vk?color=important"></a>
<a href="https://github.com/blackcatprog/comm-bot-vk/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green" height="20"></a>
<img src="https://img.shields.io/badge/Platforms-Windows%20%7C%20Android%20%7C%20Linux-blue" height="20">
</p>

## Документация

* [Инструкция для Windows](#win-instruct)
* [Инструкция для Android](#andro-instruct)
* [Инструкция для Soucre (исходного кода)](#source-instruct)
	* [Windows](#source-win-instruct)
	* [Android](#source-andro-instruct)

## Инструкция для Windows <a name="win-instruct"></a>

1) Скачиваем архив с программой:

![5](img/5.png)

<hr>

![6](img/6.png)

2) Распаковываем

3) Запускаем comm-bot-win.exe из папки Windows

4) Вводим необходимые данные (Инструкции по получению токена и id поста и пользователя ниже, они одинаковые для Android и Windows) и ожидаем добавления комментариев

## Инструкция для Android <a name="andro-instruct"></a>

1) Скачиваем архив с программой:

![1](img/1.png)
![2](img/2.png)
![3](img/3.png)
![4](img/4.png)

2) [Скачиваем Termux](https://play.google.com/store/apps/details?id=com.termux "Скачать Termux")

3) Обновляем все доступные пакеты:

```
pkg update
pkg upgrade
```

4) Устанавливаем python:

```
pkg install python
```

5) Даём доступ к внутренней памяти:

```
termux-setup-storage
```

6) Переходим в место, куда вы распаковали архив с программой:

```
cd storage
cd shared
сd files
cd Android
```
Это подходит, если вы распаковали архив с программой в корневую папку

7) Устанавливаем всё необходимое:

```
pip install -r requirements.txt
```

8) [Получаем токен](https://vkhost.github.io "Получить токен")<br>Выберите Vk Admin и скопируйте часть адресной строки от access_token= до &expires_in

9) Получаем id пользователя и id поста<br>Для этого скопируйте ссылку на пост (id пользователя от wall до _ , а id поста - всё после _

10) Запускаем скрипт:

```
python comm-bot-vk.py
```

11) Вводим все необходимые данные и ждём добавления комментариев

## Запуск из Source <a name="source-instruct"></a>

### Для Windows <a name="source-win-instruct"></a>

1) Скачиваем архив с программой (скриншоты выше)

2) Распаковываем

3) [Устанавливаем Python с официального сайта](https://python.org "Установить Python") (если у вас не установлен)

4) Нажимаем Win+R, вводим cmd и нажимаем Enter

5) Переходим в папку с программой (Нужно перейти туда, куда вы распаковали архив и открыть папку Source)<br>Ниже приведён пример с папкой на рабочем столе

```
cd Desktop
cd Source
```

6)  Устанавливаем всё необходимое:

```
pip install -r requirements.txt
```

8) Вписываем всё необходимое в cfg.ini (Инструкции по получению токена и id поста и пользователя выше, они одинаковые для Android и Windows)

9) В консоли вводим:

```
python comm-bot-vk.py
```

и выбираем сколько нужно комментариев и ожидаем добавления комментариев

###  Для Android <a name="source-andro-instruct"></a>

1) Повторяем с 1 по 9 пункты [этой инструкции](#andro-instruct)

2) Вписываем всё необходимое в cfg.ini (Инструкции по получению токена и id поста и пользователя выше, они одинаковые для Android и Windows)

3) Запускаем скрипт, вводим желаемое количество количество комментариев и ожидаем добавления комментариев
