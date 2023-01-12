from random import randint
import telebot
import time
import bot_token 
bot = telebot.TeleBot(bot_token.token)
import requests
import json



class Player(object):

	def __init__(self) -> None:
		self.player_name = 'new_player'
		self.player_id = 0
		self.player_chat_id = 0
		self.candys_pool = 0


	def set_player(self, player_name, player_id, chat_id, candys_pool) -> None:#
		self.player_name = player_name
		self.player_id = player_id
		self.player_chat_id = chat_id
		self.candys_pool = candys_pool
	
	def get_name(self):
		return self.player_name

	def get_chat_id(self):
		return self.player_chat_id

	def get_player_id(self):
		return self.player_id

	def get_name_by_id(self, id):
		if id == self.player_id:
			return self.player_name
		else: return False

	def get_candys(self):
		return self.candys_pool
	
	def parse_tele_message(self, message):
		self.player_name = message.from_user.username
		self.player_id = message.from_user.id
		self.player_chat_id = message.chat.id
		

class Game:
	def __init__(self) -> None:
		self.player1 = 0
		self.player2 = 0
		self.candys = 0
		self.last_step = 0
		pass
	def set_game_player(self, player1: Player, player2: Player, candys = 0) -> None:#
		self.player1 = player1
		self.player2 = player2
		self.candys = candys

	def game_player1_step(self, candys: int):
		self.candys -= candys
		self.player1.candys_pool += candys

	def game_player2_step(self, candys: int):
		self.candys -= candys
		self.player1.candys_pool += candys
	
	def player_name_by_id(self, player_id):
		for player in (player1, player2):
			res = player.get_name_by_id(player_id)
			if res:
				return res
	
	def get_game_player1(self):
		return self.player1

	def get_game_player2(self):
		return self.player2

	def get_game_players(self):
		return (self.player1, self.player2)
	
	def get_game_players_id(self):
		return (self.player1.get_player_id(), self.player2.get_player_id())

	def game_message_parse(self, message):
		# if self.player1.player_id == 0 and self.player2.player_id == 0:

		if self.player1.player_id != 0 and self.player2.player_id != 0:
			print('game_message_parse id1 !=0 and id2 != 0')
			if message and message.text and message.text[:5:] == '/game' and message.text[6::].isdigit():
				candys = int(message.text[6::])
				if 0 < candys < 28:
					if message.from_user.id == self.player1.player_id:
						self.game_player1_step(candys)
					elif message.from_user.id == self.player2.player_id:
						self.game_player2_step(candys)
					return self.candys, candys
				else: return self.candys, 0
			else: return self.candys, 0
		else: return Exception("Game not found!"), ''


player1 = Player()
player2 = Player()
games_pool = list()

player_cheker = 0

def player_init(message):
	player = Player()
	player.parse_tele_message(message=message)
	return player

def game_add(candys, player1: Player, player2: Player):
	game = Game()
	game.player1 = player1
	game.player2 = player2
	game.candys = candys
	return game

def game_init():
	global player1, player2, games_pool
	games_pool.clear()
	player1.set_player('player1',0,0,0)
	player2.set_player('player2',0,0,0)
	games_pool.append(game_add(candys=0, player1=player1, player2=player2))

def game_find(game_pool: list, message):
	for game_f in game_pool:
		if message.from_user.id in game_f.get_game_players_id():
			return game_pool.index(game_f)
	return -1


@bot.message_handler(commands=['stopgame'])
def game_stop(message):
	res_game_index = game_find(games_pool, message)
	if res_game_index > -1:
		games_pool.clear()
		player1.set_player('player1',0,0,0)
		player2.set_player('player2',0,0,0)
		games_pool.append(game_add(candys=0, player1=player1, player2=player2))
		bot.send_message(message.chat.id, 'Игра сброшена!')
		print(player1.get_player_id(),'\n', player2.get_player_id(), '\n', games_pool.__dir__)

@bot.message_handler(commands=['game'])
def game_start(message):
	print(message.date)
	with open('log.txt', 'a') as file:
		file.write('{};{};{};{};{}\n'.format(
			time.asctime(time.localtime(time.time())), 
			message.date, 
			message.chat.id, message.from_user.id, message.from_user.username))
	global player1, player2, games_pool
	res_game_index = game_find(games_pool, message)
	candys = 0

	if games_pool[res_game_index].player1.get_player_id() != 0 and games_pool[res_game_index].player2.get_player_id() != 0:
		if message.from_user.id not in (games_pool[res_game_index].player1.get_player_id(), games_pool[res_game_index].player2.get_player_id()):
			_player1 = Player()
			_player2 = Player()
			_player1.set_player('player1',0,0,0)
			_player2.set_player('player2',0,0,0)
			games_pool.append(game_add(candys=0, player1=_player1, player2=_player2))



	if res_game_index > -1:
		if games_pool[res_game_index].player1.get_player_id() != 0 and games_pool[res_game_index].player2.get_player_id() != 0:
			last_step = games_pool[res_game_index].last_step
			if games_pool[res_game_index].player1.get_player_id() == message.from_user.id:
				next_step = 1
			elif games_pool[res_game_index].player2.get_player_id() == message.from_user.id:
				next_step = -1
			if last_step != next_step :

				candys_before = games_pool[res_game_index].candys
				res, candys_move = games_pool[res_game_index].game_message_parse(message)
				if 0 < res < candys_before:
					bot.reply_to(message, 
						'Игра {}\nИгрок {}, забирает {} конфет, остаток {} конфет'.format(
																						res_game_index, 
																						games_pool[res_game_index].player_name_by_id(message.from_user.id),
																						candys_move, res))
					games_pool[res_game_index].last_step *= -1
					print(last_step)
				elif res < 1:
					bot.reply_to(message, 
						'Игра {}\nИгрок {}, забирает {} конфет, остаток {} конфет. Поздравляем!'.format(
																						res_game_index, 
																						games_pool[res_game_index].player_name_by_id(message.from_user.id),
																						candys_before, 0))
					bot.reply_to(message, 'ВЫ победитель!')
					game_stop(message)
			else: bot.reply_to(message, 'ХОД не ВАШ')
			pass



	
	if games_pool[len(games_pool)-1].player1.get_player_id() == 0:
		print('if num 3')
		candys = randint(114, 120)
		player1 = player_init(message)
		# player1 = player_init(message=message)
		games_pool[len(games_pool)-1].player1=player1
		games_pool[len(games_pool)-1].candys =candys
		bot.reply_to(message,'{}, вы добавлены в игру'.format(player1.get_name()))
	elif games_pool[len(games_pool)-1].player2.get_player_id() == 0 and games_pool[len(games_pool)-1].player1.get_player_id() != 0:
		print('elif num1 from if 3')
		player2 = player_init(message=message)
		bot.reply_to(message,'{}, вы добавлены в игру к {}'.format(player2.get_name(), player1.get_name() ))
		games_pool[len(games_pool)-1].player2 = player2
		first = randint(1, 100)
		if first%2 == 0:
			bot.send_message(message.chat.id, 'В Игре между {} и {}, первый ход будет за {}'.format(player1.get_name(), player2.get_name(), player2.get_name()) )
			games_pool[len(games_pool)-1].last_step = 1
		else: 
			bot.send_message(message.chat.id, 'В Игре между {} и {}, первый ход будет за {}'.format(player1.get_name(), player2.get_name(), player1.get_name()) )
			games_pool[len(games_pool)-1].last_step = -1
		bot.send_message(message.chat.id, 'Игра за {} конфет, между {} и {} начинается...'.format(games_pool[len(games_pool)-1].candys, player1.get_name(), player2.get_name()))
		
	else:
		print('else from if 3 under elif num1') 
		pass


	bot.send_message(message.chat.id, "тут текст для проверки")

def game_step(message):
	global player1, player2, candys
	print(message.text, end=' - ')
	print(message.text[6::])
	try:
		eat_candy = int(message.text[6::])

		if message.chat.id == player1:
			if eat_candy <29 and eat_candy > 0:
				candys -= eat_candy
			if candys <= 0:
				bot.reply_to(message, ' ВЫ ПОБЕДИТЕЛЬ!')
				player1 = 0
				player2 = 0
			elif eat_candy<29 and eat_candy > 0:
				bot.reply_to(message, f' осталось {candys} конфет')
			else: bot.reply_to(message, f' не больше 28 конфет и не меньше 1')
	except: bot.reply_to(message, "используйте целые числа для игры!")




def send_welcome(message):
	
	global player1, player2, candys
	print("---------------INIT---------------")
	print(str(message.text).find('game'))
	print(message.text)
	print(player1)
	print(player2)

	if str(message.text).find('game') == 1:
		# if message.chat.id not in [player1, player2]:
			if len(message.text) == 5:
				if player1 == 0:
					player1 = int(message.from_user.id)
					bot.send_message(player1, 'Вы добавлены в игру')
				elif player2 == 0:
					player2 = int(message.from_user.id)
					bot.send_message(player2, 'Игра начнется через :')
					for i in range(1,4):
						time.sleep(0.7)
						bot.send_message(message.chat.id, i)
					game_start(message)
					
				
			if len(message.text) > 5:
				game_step(message)	
	
	
@bot.message_handler(commands=['exchange'])
def exchange(message):
	link = 'https://www.cbr-xml-daily.ru/daily_json.js'
	r = requests.get(link)
	text = json.loads(r.text)
    #print(text)
	res = r.text.find('CBR_XML_Daily_Ru')+ len('CBR_XML_Daily_Ru') + 1
    #print(res)
	result = json.loads(r.text[::])
	print(result['Valute']['USD'])
	result2 = dict(result)
	value_list = list()
	for item in result2['Valute'].items():
		value_list.append(item[0])
	print(value_list)
	print(message.text[10:13:])
	# print(value_list.index(message.text[10:13:].upper()))
    # print(result2['Valute'].items())
	if len(message.text[10:13:].upper())>2 and message.text[10:13:].upper() in value_list:
		bot.reply_to(message, '{} "{}" стоит {} рублей'.format(
						message.text[10:13:].upper(),
						result['Valute'][message.text[10:13:].upper()]['Name'],
						result['Valute'][message.text[10:13:].upper()]['Value']))
	else:
		bot.reply_to(message, 'Введите название валюты, пример "/exchange USD"') 
		bot.reply_to(message, "Возможные варианты: {}".format(' '.join(value_list)))



game_init()
bot.infinity_polling()
