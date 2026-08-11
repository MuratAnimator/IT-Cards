import disnake
import os
import random
import asyncio
from disnake.ext import commands
from pathlib import Path
from dotenv import load_dotenv

bot = commands.Bot(command_prefix=">", help_command=None, intents=disnake.Intents.all())

Cards = [
"Баг 404", "Джуниор-стажер", "кнопка Пуск в Windows", "Cntrl+C",
"Баг 500 (Internal Error)", "Мидл-разработчик", "Docker-контейнер", "Git commit -m 'fix'",
"OutOfMemoryException", "Сениор-Архитектор", "Kubernetes-кластер", "Git push --force в мастер",
"Легаси-код 1988 года", "Тимлид-каратель", "Сервер, который работал 10 лет без перезагрузки", "Дедлайн, который перенесли"
]
cardFiles = {
	"Баг 404": "bug404.png",
	"Джуниор-стажер": "junior.png",
	"кнопка Пуск в Windows": "startButton.png",
	"Cntrl+C": "CntrlC.png",
	"Баг 500 (Internal Error)": "bug500.png",
	"Мидл-разработчик": "MiddleDev.png",
	"Docker-контейнер": "Docker.png",
	"Git commit -m 'fix'": "Git1.png",
	"OutOfMemoryException": "OutOfMemoryException.png",
	"Сениор-Архитектор": "Senior.png",
	"Kubernetes-кластер": "Kubernetes.png",
	"Git push --force в мастер": "Git2.png",
	"Легаси-код 1988 года": "CodeOf1988Year.png",
	"Тимлид-каратель": "TeamLead.png",
	"Сервер, который работал 10 лет без перезагрузки": "ServerOfTenYears.png",
	"Дедлайн, который перенесли": "DeadLine.png"
}

@bot.event
async def on_connect():
	print("Идем в Дискорд... ")
@bot.event
async def on_ready():
	print("Бот включен!")
@bot.event
async def on_disconnect():
	print("Бот вырубился из-за ошибки в фиг пойми где")

@bot.command()
async def card(ctx):
	
	card = random.choice(Cards)
	filename = cardFiles.get(card)
	if filename:
		cardsPath = Path("cardsImages") / filename
		await ctx.send("Вытаскиваю карту...")
		await asyncio.sleep(1)
	
		if cardsPath.exists():
			file = disnake.File(cardsPath, filename="card.png")
			await ctx.send(
			f"Поздравляю {ctx.author.name}, ты получил карту '{card}'!",
			file=file
			)
		else:
			await ctx.send(f"Поздравляю {ctx.author.name}, ты получил карту '{card}'! (файл не найден)")

@bot.command()
async def cardList(ctx):
	await ctx.send(f"""
	Список всех карточек в боте:
	Обычная редкость ↓
	'Баг 404', 'Джуниор-Стажер', 'кнопка Пуск в Windows', 'Cntrl+C'
	Эпическая редкость ↓
	'Баг 500 (Internal Error)', 'Мидл-разработчик', 'Docker-контейнер', 'Git commit -m fix'
	Мифическая редкость ↓
	'OutOfMemoryException', 'Сениор-Архитектор', 'Kubernetes-кластер', 'Git push --force в мастер'
	Легедарная редкость ↓
	'Легаси-код 1988 года', 'Тимлид-каратель', 'Сервер, который работал 10 лет без перезагрузки', 'Дедлайн, который перенесли'
	"""
	)

@bot.command()
async def help(ctx):
	await ctx.send("""
	Список команд в боте IT Cards:
	>help список команд
	>card получить карту
	>cardList список всех карточек, которые можно получить в боте
	"""
	)

script_dir = Path(__file__).parent
env_path = script_dir / ".env"
load_dotenv(env_path)
bot.run(os.getenv('TOKEN'))