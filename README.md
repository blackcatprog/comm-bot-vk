<p align="center"><h1>Comm-Bot-Vk</h1></p>

## Инструкция для Windows

## Инструкция для Android

1) Скачиваем архив с программой:



1) Скачиваем Termux по ссылке - 

2) Обновляем все доступные пакеты:

```
pkg update && pkg upgrade
```

3) Устанавливаем python:

```
pkg install python
```

3) Даём доступ к внутренней памяти:

```
termux-setup-storage
```

5) [Получаем токен](https://vkhost.github.io "Получить токен")<br>Выберите Vk Admin и скопируйте часть адресной строки от access_token= до &expires_in

6) Получаем id пользователя и id поста<br>Для этого скопируйте ссылку на пост (id пользователя от wall до _ , а id поста - всё после _

7) В Termux вводим 
