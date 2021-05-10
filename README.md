# comm-bot-vk

## Инструкция для Windows

## Инструкция для Android

1) Скачиваем Termux по ссылке - 

2) Обновляем все доступные пакеты:

```
pkg update && pkg upgrade
```

3) Даём доступ к внутренней памяти:

```
termux-setup-storage
```

4) Переходим по тому пути, где у вас находится папка <<Android>> из распакованного архива:

```
cd storage
cd shared
cd Android
```

5) [Получаем токен](https://vkhost.github.io "Получить токен")  Выберите Vk Admin и скопируйте часть адресной строки от access_token= до &expires_in
