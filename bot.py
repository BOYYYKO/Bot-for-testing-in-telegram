import telebot
import random
import time
import datetime
from datetime import datetime
from telebot import types

correct_count = 0
count = 0

date = 0

res2 = 0
res1 = 0
res0 = 0 

sec1 = 0
min1 = 0
hour1 = 0
i = 0

TOKEN = '2127431193:AAFFUcL03tmD9wjvj1sRLkcm_03bwUPyh54'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/sticker.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("👀 Розпочати тестування")
 
	markup.add(item1)

	bot.send_message(message.chat.id, ' Вітаю, {0.first_name}🦾\nЯ - <b> бот</b>, який протестує тебе\nНехай удача завжди буде з вами!🐙'.format(message.from_user, bot.get_me()),
		 parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def test(message):
	global date
	global res0
	global res1
	global res2

	if message.chat.type == 'private':

		if message.text == '😊 Дізнатися час':
			bot.send_message(message.chat.id, f'Ви пройшли тест за {res0} год {res1%60} хв {res2%60%60} сек | {date}\n')

		elif message.text == '👀 Розпочати тестування' or message.text == '👀 Знову розпочати тестування':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("❌ Закінчити тест")
			markup.add(item1)
			bot.send_message(message.chat.id, 'Тест розпочато...'.format(message.from_user),
				parse_mode='html', reply_markup=markup)

			global sec1
			global min1
			global hour1

			now=datetime.now()
			sec1=now.strftime("%S")
			min1=now.strftime("%M")
			hour1=now.strftime("%H")

			arr = []
			global correct_count
			global count
			global i
			correct_count = 0
			count = 0
			i = 0

			for j in range(10):
				arr.append(j+1)

			random.shuffle(arr)

			def set_question(question, variant1, variant1_callback, variant2, variant2_callback, variant3, variant3_callback, variant4, variant4_callback):
				markup = types.InlineKeyboardMarkup(row_width=4)
				answer1 = types.InlineKeyboardButton(variant1, callback_data=variant1_callback)
				answer2 = types.InlineKeyboardButton(variant2, callback_data=variant2_callback)
				answer3 = types.InlineKeyboardButton(variant3, callback_data=variant3_callback)
				answer4 = types.InlineKeyboardButton(variant4, callback_data=variant4_callback)
				markup.add(answer1, answer2, answer3, answer4)
				bot.send_message(message.chat.id, question, reply_markup=markup)

			def questionbase(i):
				if i == 1: set_question('Який з наведених варіантів є вірним оголошенням private поля?\n\n1️⃣   private field = 0\n2️⃣   field = 0\n3️⃣   _field = 0\n4️⃣   __field = 0','1️⃣','-','2️⃣','+','3️⃣','-','4️⃣','-')
				elif i == 2:
					img = open('static/question2.jpg', 'rb')
					bot.send_sticker(message.chat.id, img)
					set_question('Що виведе код?\n\n1️⃣   СanineError: Dog malfunction\n2️⃣   Woof!\n3️⃣   Arff!\n4️⃣   *walkin*','1️⃣','-','2️⃣','-','3️⃣','+','4️⃣','-')
				elif i == 3: set_question('Як створити конструктор класу А?\n\n1️⃣   A(Параметри конструктора)\n2️⃣   def __init__(Параметри конструктора)\n3️⃣   def __A__(Параметри конструктора)\n4️⃣   def init(Параметри конструктора)','1️⃣','-','2️⃣','+','3️⃣','-','4️⃣','-')
				elif i == 4: set_question('Знайди правильний запис\n\n1️⃣   <екземпляр класу>.<ім’я методу> ([параметри])\n2️⃣   <ім’я методу>.<екземпляр класу> ([параметри])\n3️⃣   <ім’я методу>.<параметри> (екземпляр клас[у])\n4️⃣   <ім’я методу><параметри>.(екземпляр клас[у])','1️⃣','-','2️⃣','+','3️⃣','-','4️⃣','-')
				elif i == 5: set_question('Що означає параметр self у заголовку методу?\n\n1️⃣   Назву події\n2️⃣   Значення властивості об’єкта\n3️⃣   Замість параметра self підставляється ім’я об’єкта\n4️⃣   Замість параметра self підставляється ім’я події','1️⃣','-','2️⃣','-','3️⃣','+','4️⃣','-')
				elif i == 6: set_question('Клас - це\n\n1️⃣   Тип величин\n2️⃣   Опис об’єктів певного типу\n3️⃣   Опис характеристик об’єкта\n4️⃣   Метод розв’язування задачі','1️⃣','-','2️⃣','+','3️⃣','-','4️⃣','-')
				elif i == 7: set_question('Екземпляр деякого класу це\n\n1️⃣   Тип\n2️⃣   Підклас\n3️⃣   Варіант\n4️⃣   Об‘єкт','1️⃣','-','2️⃣','-','3️⃣','-','4️⃣','+')
				elif i == 8: set_question('Як звернутися до значення атрибута name екземпляра my_school?\n\n1️⃣   name(my_school)\n2️⃣   name.my_school\n3️⃣   name.my_school\n4️⃣   my_school_name','1️⃣','-','2️⃣','-','3️⃣','+','4️⃣','-')
				elif i == 9: 
					img = open('static/question9.jpg', 'rb')
					bot.send_sticker(message.chat.id, img)
					set_question('У якому операторі правильно створюється екземпляр класу B()?\n\n1️⃣   my_b = B("Клас", 10)\n2️⃣   my_b = B("Тетяна", "Марина", 10)\n3️⃣   my_b = B(Тетяна, Марина, 10)\n4️⃣   my_b = B("Тетяна", "Марина")','1️⃣','-','2️⃣','+','3️⃣','-','4️⃣','-')
				elif i == 10: set_question('На основі класу можна створити\n\n1️⃣   Cтільки екземплярів, скільки вам буде потрібно\n2️⃣   Два екземпляри\n3️⃣   Тільки один екземпляр\n4️⃣   Не можна їх створити','1️⃣','+','2️⃣','-','3️⃣','-','4️⃣','-')

			def next_question():
				global i
				if i<9:
					i+=1
					questionbase(arr[i])

			questionbase(arr[i])

			@bot.callback_query_handler(func=lambda call: True)
			def callback(call):
				global correct_count
				try:
					if call.message:
						if call.data == '+':
							correct_count += 1
							alert(call, call.message)
						elif call.data == '-':
							alert(call, call.message)

				except Exception as e:
					print(repr(e))

			def alert(call, message):
				global count
				count += 1
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
					text="Відповідь зараховано...")

				next_question()
				if count == 10:
					markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
					item2 = types.KeyboardButton("✅ Отримати результат")
					markup.add(item2)
					bot.send_message(message.chat.id, ' Ви повністю закінчили проходження тесту✨\nБажаєте отримати результат?'.format(message.from_user),
						parse_mode='html', reply_markup=markup)

		elif message.text == '✅ Отримати результат' or message.text == '❌ Закінчити тест':
			sti = open('static/sticker2.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)

			date = datetime.now().date()
			now = datetime.now()
			sec2 = now.strftime("%S")
			min2 = now.strftime("%M")
			hour2 = now.strftime("%H")

			hourr1 = int(hour1)
			hourr2 = int(hour2)
			hour = hourr2-hourr1
			res0 = hour

			min1hour1 = int(hour1*60+min1)
			min2hour2 = int(hour2*60+min2)
			minres1 = min2hour2-min1hour1
			res1 = minres1%60

			sec1min1hour1 = int(hour1*60+min1*60+sec1)
			sec2min2hour2 = int(hour2*60+min2*60+sec2)
			res2 = sec2min2hour2 - sec1min1hour1

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("👀 Знову розпочати тестування")
			item2 = types.KeyboardButton('😊 Дізнатися час')
			markup.add(item1, item2)
			bot.send_message(message.chat.id, f'Ваш результат -  <b>вірних {correct_count} із {count} запитань</b>'.format(message.from_user),
				parse_mode='html', reply_markup=markup)

		else:
			bot.send_message(message.chat.id, 'Я не знаю, що відповісти 😢')

# RUN
bot.polling(none_stop=True)