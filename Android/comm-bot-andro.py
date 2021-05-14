import vk_api
import time
from colorama import Fore

def graph():
	print("                COMMENTS BOT (by blackcat)")
	print("            author on vk: https://vk.com/krtvx")
	print("     author on github: https://github.com/blackcatprog\n")

def func():
	try:
		token = input("Токен пользователя: ")
		user = input("Введите id пользователя на стене у которого находится пост: ")
		post = input("Введите id записи: ")
		text = input("Введите текст комментария: ")
		comms = input("Сколько накрутить комментариев: ")
		times = input("Введите задержку перед отправкой комментария: ")

		session = vk_api.VkApi(token = token)

		comms = int(comms)
		num1 = 0

		while num1 < comms:
			session.method("wall.createComment", {
				"owner_id": user,
				"post_id": post,
				"message": text,
				})
			time.sleep(times)
			num1 += 1
			print(f"Добавлено: {num1} " + "комментариев" + "\r", end = "")

			if num1 == num:
				print(Fore.GREEN + "Все комментарии добавлены!")
				break
	except vk_api.exceptions.ApiError as error:
		error = str(error)
		if error[1:4] == "100":
			print(Fore.RED + "Пост отсутствует")
		elif error[1:2] == "5":
			print(Fore.RED + "Ошибка авторизации")
	except KeyboardInterrupt:
		print(Fore.RED + "\nВыполнен выход")

graph()
func()