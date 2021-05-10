import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import configparser
import time
from colorama import Fore

def graph():
	print("                COMMENTS BOT (by blackcat)")
	print("            author on vk: https://vk.com/krtvx")
	print("     author on github: https://github.com/blackcatprog\n")

def func():
	try:
		cfg = configparser.ConfigParser()
		cfg.read("cfg.ini")
		token = cfg.get("data", "token")
		user = cfg.get("data", "user")
		post = cfg.get("data", "post")
		text = cfg.get("data", "text")
		times = cfg.get("data", "time")
		times = int(times)
		
		session = vk_api.VkApi(token = token)
		i1 = input("Сколько накрутить комментариев: ")
		num = int(i1)
		num1 = 0


		while num1 < num:
			session.method("wall.createComment", {
				"owner_id": user,
				"pot_id": post,
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
		if error[0:5] == "[100]":
			print(Fore.RED + "Пост отсутствует")
	except KeyboardInterrupt:
		print(Fore.RED + "\nВыполнен выход")

graph()
func()