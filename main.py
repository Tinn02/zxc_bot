import discord
from discord.ext import commands
import json
import requests

TOKEN = 'Nzg1ODQ3NDMwMzE3ODY3MDA4.X89zcw.Qwn2hLJtzhxFBIph8b4FDBdBHF8'
bot = commands.Bot(command_prefix='!')

@bot.event # запуск бота
async def on_ready(pass_context=True):
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def тест(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

@bot.command() # приветвие
async def привет(ctx):
    await ctx.send(":smiley: :wave: Дарова!")

#--------------------------------------------------------------------------------арифмитические действия--------------------------------------------------------------------------------

@bot.command() # сложение
async def слож(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command() # умножение
async def умнож(ctx, a: int, b: int):
    await ctx.send(a*b)

#--------------------------------------------------------------------------------информационные команды--------------------------------------------------------------------------------

@bot.command() # команда !инфо
async def инфо(ctx):
    embed = discord.Embed(title="ZXC", description="Самый лучший бот", color=0x00ffff, inline=False)
    
    embed.add_field(name="Автор", value="Tinn02", inline=False)
    embed.add_field(name="Сервер автора: HALT", value="[https://discord.gg/ASmswHE]", inline=False)
    embed.add_field(name="Приглашение бота", value="[https://discord.com/api/oauth2/authorize?client_id=785847430317867008&permissions=8&scope=bot]", inline=False)
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command() # команда !помощь
async def помощь(ctx):
    embed = discord.Embed(title="Команды ZXC бота:", color=0x00cccc)

    embed.add_field(name="!помощь", value="Выдаёт это сообщение", inline=False)
    embed.add_field(name="!инфо", value="Даёт информацию о боте", inline=False)
    embed.add_field(name="!тест", value="Повторяет 1 слово после команды", inline=False)
    embed.add_field(name="!слож X Y", value="Складывает значения X и Y", inline=False)
    embed.add_field(name="!умнож X Y", value="Перемножает значения X и Y", inline=False)
    embed.add_field(name="!привет", value="Отправляет сообщение-привествие", inline=False)
    embed.add_field(name="!кот", value="Даёт рандомную фотографию кисы =3", inline=False)
    embed.add_field(name="!лиса", value="Даёт рандомную фотографию лиськи =3", inline=False)
    embed.add_field(name="!распX_Y", value="Выдаёт расписание группы\n(X - 2 последние цифры года зачисления; Y - № группы)\n P.S. на базе 11 классов в конце нужно поставить `_11` \n Расписание доступно для групп: `18_1` `18_2` `20_2_11`", inline=False)
    embed.add_field(name="!сессияX_Y", value="Выдаёт расписание сессии для группы\n(X - 2 последние цифры года зачисления; Y - № группы)\n P.S. на базе 11 классов в конце нужно поставить `_11` \n Расписание сессий доступно для `всех групп сервера!`", inline=False)

    await ctx.send(embed=embed)

#--------------------------------------------------------------------------------рандомные фото--------------------------------------------------------------------------------

@bot.command() # фотки лис
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Рандомная лися') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command() # фотки котов
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xf2f3f4, title = 'Рандомная кися') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

#--------------------------------------------------------------------------------расписание групп--------------------------------------------------------------------------------

@bot.command() # 2018-1
async def расп18_1(ctx):
    embed = discord.Embed(title="Расписание группы ИН-К-0-Д-2018-1", color=0x0f52ba)
    embed.set_image(url="https://media.discordapp.net/attachments/698478059078156319/790291983594946590/4M6uFIsha5k.png?width=629&height=703")
    await ctx.send(embed=embed)

@bot.command() # 2018-2
async def расп18_2(ctx):
    embed = discord.Embed(title="Расписание группы ИН-К-0-Д-2018-2", color=0x0f52ba)
    embed.set_image(url="https://media.discordapp.net/attachments/698478059078156319/790253695513133056/raspisanie.png?width=1303&height=678")
    await ctx.send(embed=embed)

    
@bot.command() # 2020-2-11
async def расп20_2_11(ctx):
    embed = discord.Embed(title="Расписание группы ИН-К-0-Д-2020-2-11", color=0x0f52ba)
    embed.set_image(url="https://media.discordapp.net/attachments/698478059078156319/790292215376379914/unknown.png?width=1440&height=493")
    await ctx.send(embed=embed)

#--------------------------------------------------------------------------------сессия групп--------------------------------------------------------------------------------

@bot.command() # 2018-1
async def сессия18_1(ctx):
    embed = discord.Embed(title="Расписание сессии ИН-К-0-Д-2018-1", color=0x483d8b)
    embed.set_image(url="https://media.discordapp.net/attachments/698478059078156319/790327243201052672/unknown.png")
    await ctx.send(embed=embed)

@bot.command() # 2018-2
async def сессия18_2(ctx):
    embed = discord.Embed(title="Расписание сессии ИН-К-0-Д-2018-2", color=0x483d8b)
    embed.set_image(url="https://media.discordapp.net/attachments/698478059078156319/790304332066717736/CLt4TSq-tKg.png")
    await ctx.send(embed=embed)

@bot.command() # 2019-1
async def сессия19_1(ctx):
    embed = discord.Embed(title="Расписание сессии ИН-К-0-Д-2019-1", color=0x483d8b)
    embed.set_image(url="https://media.discordapp.net/attachments/698478059078156319/790326827025432596/unknown.png")
    await ctx.send(embed=embed)

@bot.command() # 2019-2
async def сессия19_2(ctx):
    embed = discord.Embed(title="Расписание сессии ИН-К-0-Д-2019-2", color=0x483d8b)
    embed.set_image(url="https://media.discordapp.net/attachments/698478059078156319/790326906863878194/unknown.png")
    await ctx.send(embed=embed)

@bot.command() # 2020-2-11
async def сессия20_2_11(ctx):
    embed = discord.Embed(title="Расписание сессии ИН-К-0-Д-2020-2-11", color=0x483d8b)
    embed.set_image(url="https://media.discordapp.net/attachments/698478059078156319/790326970327760936/unknown.png")
    await ctx.send(embed=embed)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(340360564696154114)
    await channel.send(f"{member}, добро пожаловать! =)")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(340360564696154114)
    await channel.send(f"{member} покинул нас =(")

bot.run(TOKEN) # токен берётся из файла config.py для безопасности
