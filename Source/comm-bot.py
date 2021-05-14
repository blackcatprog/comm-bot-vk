import vk_api
import configparser
import time
from colorama import Fore
import ctypes

#support colors
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def graph():
	print("                  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+ ")
	print("                  |C O M M E N T - B O T - V K| ")
	print("                  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+ by blackcat ")
	print("")
	print("                author on vk: https://vk.com/krtvx")
	print("         author on github: https://github.com/blackcatprog\n")

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
		elif error[1:4] == "213":
			print("Нет доступа к записи")
	except configparser.ParsingError:
		print(Fore.RED + "Ошибка чтения конфига")
	except KeyboardInterrupt:
		print(Fore.RED + "\nВыполнен выход")

graph()
func()