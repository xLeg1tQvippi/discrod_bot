from discord import Interaction
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
from dotenv import load_dotenv
import os
import asyncio
from random import choices, choice
from pprint import pprint
from time import time
"""Это дискорд бот"""
GLOBAL_USER_REPEAT_LIST = [] 



def get_token():
    load_dotenv()
    BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    return BOT_TOKEN


intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)

@bot.event
async def on_ready():
    print(f"Бот: {bot.user}, готов к работе!")

@bot.command()
async def run_timer(ctx):
    while True:
        await asyncio.sleep(3600)
        await random_kick(ctx)
    

@bot.command(aliases=[r'/seppuku'])
async def seppuku(ctx):
    author_id = ctx.author.id
    await voicekick(ctx, author_id)
    # await ctx.reply(f"{ctx.author.display_name} совершает /seppuku!\nПрощай {ctx.author.display_name}... Мы тебя забудем D:")
    seppuku_gif = choice([r'https://media.discordapp.net/attachments/1196107826427338866/1293180977983656058/togif.gif?ex=6947e123&is=69468fa3&hm=579d9974db8de6dcd34f025da8cf8c9aa5877515af0c77b7fbbabba2d203cfe8&=&width=400&height=400', r'https://media.discordapp.net/attachments/880730952337354783/1126853248859516958/attachment-10.gif?ex=6947e8de&is=6946975e&hm=2e140db6ddc7d9f3b8bb568cc90dc0ef7c4be149ef0063ded26f190b652d2405&=&width=640&height=846'])
    await ctx.reply(seppuku_gif)
    
    

@bot.command(aliases=["Привет!", "привет", "Привет", "Hello", "hello!", "Hello!"])
async def hello(ctx):
    """Приветствует пользователя"""
    author = ctx.author.display_name
    await ctx.reply(f"Приветик, {author}!")

@bot.command(aliases=["Расскажи о создателе", "создатель", "who_is_the_creator"])
async def tell(ctx):
    """Рассказывает о создателе"""
    await ctx.reply(
        f"Моим создателем и героем является... *звук барабанных палок*... Облачко! а точнее - @doesitreal!"
    )
    # if message == "хм".lower():
    #     await ctx.reply("Что-то не так?")

@commands.has_permissions(manage_channels=True)
async def voicemove(ctx, member_id: int):
    """
    Кикает пользователя из голосового канала
    Использование: !voicekick @пользователь
    """
    member = await ctx.guild.fetch_member(member_id)
    # Проверяем, находится ли пользователь в голосовом канале
    if member.voice is None or member.voice.channel is None:
        await ctx.send(f"{member.mention} не находится в голосовом канале!")
        return
    
    voice_channel_to_be_moved_in: str = choice(ctx.guild.voice_channels)
    # Отключаем пользователя от голосового канала
    await member.move_to(voice_channel_to_be_moved_in)
    await ctx.send(f"{member.mention} был перемещен в {voice_channel_to_be_moved_in}!")

@commands.has_permissions(manage_channels=True)
async def voicekick(ctx, member_id: int):
    """
    Кикает пользователя из голосового канала
    Использование: !voicekick @пользователь
    """
    member = await ctx.guild.fetch_member(member_id)
    # Проверяем, находится ли пользователь в голосовом канале
    if member.voice is None or member.voice.channel is None:
        # await ctx.send(f"{member.mention} не находится в голосовом канале!")
        return
    
    # Отключаем пользователя от голосового канала
    await member.move_to(None)
    # await ctx.send(f"{member.mention} был отключен от голосового канала!")
HOW_ARE_PHRASES = [
    'как дела', 'как ты', 'как делишки',
    'хей как дела', 'хей как ты', 
    'привет как дела', 'привет как ты',
    'как дела?', 'как ты?', 'как делишки?',
    'как твои дела', 'как жизнь'
]

# @bot.event
# async def on_message(message):
#     if message.author.bot:
#         return
    
#     # Проверяем, содержит ли сообщение одну из фраз
#     content = message.content.lower().strip()
    
#     for phrase in HOW_ARE_PHRASES:
#         if phrase in content:
#             await message.channel.send(f"Привет, {message.author.display_name}!, Уум.. У меня дела всегда прекрасно! ..Ну почти)\nЧто на счет вас, {message.author.display_name}, как дела у вас? ^^")
#             author_name = message.author
#             def check(m):
#             # Проверяем, что ответ от того же пользователя в том же канале
#                 return m.author == message.author and m.channel == message.channel
            
#             try:
#                 # Ждем ответ 30 секунд
#                 msg = await bot.wait_for('message', timeout=30.0, check=check)
                
#                 # Анализируем ответ
#                 response = msg.content.lower()
                
#                 if any(word in response for word in ['хорошо)', "хорошо", 'отлично', 'отлично)' 'прекрасно', 'отлично', 'супер', 'класс']):
#                     await message.channel.send(f"Рада слышать ^^ {author_name}! Продолжайте в том же духе!")
#                 elif any(word in response for word in ['плохо', 'ужасно', 'не очень', 'грустно', 'скучно']):
#                     await message.channel.send(f"Ох, {author_name}, надеюсь, всё наладится! Если нужно поболтать - я тут.")
#                 elif any(word in response for word in ['нормально', 'норм', 'ок', 'сойдет', 'так себе']):
#                     await message.channel.send(f"Нуу.. нормально - это тоже неплохо, {author_name}!")
#                 else:
#                     await message.channel.send(f"Интересненнькоо.., {author_name}. Спасибо большое, что поделились! ^^")
                    
#             except asyncio.TimeoutError:
#                 pass
                
# @bot.command(aliases=['Как дела?', 'Как ты?', 'Как ты', 'как ты', 'как дела?', 'как дела', "хей, как ты?", "хей как ты", "хей, как дела", 'хей, как дела?', "Хей, как дела?", 'Как делишки?', 'как делишки?'])
# async def how_are_you(ctx):
    

async def voiceusers(ctx, author_id: int):
    """Показать всех пользователей в голосовых каналах"""
    print('GLOBAL LIST CHECK:', GLOBAL_USER_REPEAT_LIST)
    # Список для хранения информации
    voice_users = []
    voice_users_id = []
    # Проходим по всем голосовым каналам сервера
    for voice_channel in ctx.guild.voice_channels:
        if voice_channel.members:  # Если в канале есть пользователи
            for member in voice_channel.members:
                voice_users.append({
                    'member': member,
                    'channel': voice_channel,
                })
                voice_users_id.append(member.id)

    user_initiated_kick: str = await bot.fetch_user(author_id)
    
    if not voice_users:
        return

    if author_id not in voice_users_id:
        not_in_voice_kick_answers: list = [
                                           f"Нет, я конечно все понимаю.. команда для всех, все честно, но.. использовать вне войса как то не честно, {user_initiated_kick.display_name}.",
                                           f"Я безумно была уверена в том, что эту команду должны использовать находясь в войсе {user_initiated_kick.display_name}",
                                           f"Ну.. как-то не справедливо, что вы, {user_initiated_kick.display_name} не находитесь в войсе, и пытаетесь кого-то кикнуть, ну.. имейте совесть("
                                           ]
        
        await ctx.reply(choice(not_in_voice_kick_answers))
    
        return
    if GLOBAL_USER_REPEAT_LIST:        
        selfkickanswer: list = [f"Ну.. куда ты так часто то используешь эту команду.. Ай-яй-яйй.. {user_initiated_kick.display_name}!",
                                f"Ну.. Лично я считаю, карма берет свое, не так-ли {user_initiated_kick.display_name}? :D",
                                f"Ха-ха, смешно, давай не так часто использовать эту команду, {user_initiated_kick.display_name}?",
                                f"Я конечно не эксперт, но помойму злоупотребление этой командой приводит не к самым лучшим последствиям, {user_initiated_kick.display_name} ^^"
                                ]
        
        if author_id in GLOBAL_USER_REPEAT_LIST:
            await ctx.reply(choice(selfkickanswer))
            await voicekick(ctx, author_id)
            return
    
    GLOBAL_USER_REPEAT_LIST.append(author_id)
    
    
    # Формируем сообщение
    message = "И так посмотрим.. кто тут у нас:\n\n"
    
    # Группируем по каналам
    channels_dict = {}
    for user in voice_users:
        channel_name = user['channel'].name
        if channel_name not in channels_dict:
            channels_dict[channel_name] = []
        channels_dict[channel_name].append(user['member'].display_name)
    
    # Выводим сгруппированную информацию
    users_data = {}
    voice_members = []
    
    message1 = None
    message2 = None
    
    for channel in ctx.guild.voice_channels:
        voice_members.extend(channel.members)
    
    
    members_info = []
    for member in voice_members:
        channel = member.voice.channel
        info = {
            'id': member.id,
            'name': member.display_name,
            'tag': str(member),
            'channel': channel.name,
            'channel_id': channel.id,
            'joined_at': member.voice.deaf or "Нет данных",
            'is_muted': member.voice.mute,
            'is_deafened': member.voice.deaf
        }
        members_info.append(info)
        
    return members_info, GLOBAL_USER_REPEAT_LIST
    
    # for channel_name, users in channels_dict.items():
    #     message1 += f"В '{channel_name}' кажется.. сидят столько человек: ({len(users)}):\nА вот они)\n"
    #     message2 += ", ".join(users)
    # else:
    #     await ctx.send(message1)
    #     await ctx.send(message2)

@bot.command()
async def random_kick(ctx):
    author_id = ctx.author.id
    members_info, GLOBAL_USER_REPEAT_LIST = await voiceusers(ctx, author_id)
    try:
        members_id_list, chances_list = await create_chances_on_members(members_info=members_info)
    except Exception:
        pass
    chosen_person: int = choices(members_id_list, weights=chances_list, k=1)
    
    user = await bot.fetch_user(chosen_person[0])
    
    answers = [f'Сектор сегодняшнего войса на барабане... Оп! Это: {user.display_name}! К слову на тебя был маленький шанс :)',
               f'Пау-Пиу по {user.display_name}! Я победила ^^',
               f"Извини, {user.display_name}, придется тебя вытащить с войса... :с"
               f"Крутим револьвер... стреляем.. А, стоп, он же полностью заряженный! *Щелчок* (Под выстрел попал: {user.display_name}) Упс..."
               ]
    
    await ctx.reply(choice(answers))
    await voicekick(ctx, *chosen_person)
    print('GLOBAL USER REPEAT LIST:', GLOBAL_USER_REPEAT_LIST)
    await asyncio.sleep(60)
    print(f'global list has been reset! previous: {GLOBAL_USER_REPEAT_LIST}')
    GLOBAL_USER_REPEAT_LIST.clear()
    print(f"current: {GLOBAL_USER_REPEAT_LIST}")
    

async def create_chances_on_members(members_info: list[dict]) -> list | list:
    chances_list = []
    members_id_list = []
    chance = 0
    try:
        total_members = len(members_info)
        for info in members_info:
            print('current user:', info["name"])
            if info['name'] == "guccibruh":
                chance = 25
                chances_list.append(chance)
                members_id_list.append(info["id"])
                continue
            elif info['id'] == 855011610317815858:
                chance = 1
                chances_list.append(chance)
                members_id_list.append(info["id"])
                continue
            elif info['id'] == 696997056602046484:
                chance = 1
                chances_list.append(chance)
                members_id_list.append(info["id"])
                continue
            elif info['id'] == 961302430367223889:
                chance = 1
                chances_list.append(chance)
                members_id_list.append(info["id"])
                continue
            elif info['id'] == 1191003763545219103:
                chance = 25
                chances_list.append(chance)
                members_id_list.append(info['id'])
            else:
                chance = (100//total_members)
                chances_list.append(chance)
                members_id_list.append(info["id"])
            print("his chance to be kicked:", chance)
        else:
            print(members_id_list, chances_list)
            return members_id_list, chances_list
    except Exception as error:
        pass
    
@bot.command(aliases=["таймер"])
async def timer(ctx, *, time: str):
    time: str = time.lower()
    time_sign: str = time[-1]
    if time.endswith("s"):
        seconds = int(time[:-1])
    elif time.endswith("m"):
        seconds = int(time[:-1]) * 60
    elif time.endswith("h"):
        seconds = int(time[:-1]) * 60 * 60
    else:
        await ctx.reply("Неверный формат времени!")
        return
    await ctx.reply(f"Таймер установлен на {time} !")

    await asyncio.sleep(seconds)
    await ctx.reply(f"Время вышло!")
    await random_kick(ctx)


# about member


@bot.command(aliases=["Аватар", "аватар"])
async def avatar(ctx, user: discord.Member = None):
    """Возвращает аватар пользователя"""
    if user is None:
        user = ctx.author  # Если не был передан аргумент, используем автора команды
    await ctx.reply(f"Аватар пользователя {user.display_name}:\n{user.avatar.url}")


@bot.command()
async def расскажи_о(ctx, user: discord.Member):
    # Получаем информацию о пользователе
    """Информация о пользователе"""
    await ctx.reply(
        f"Информация о пользователе {user.display_name}:\n"
        f"Имя: {user.name}\n"
        f"ID: {user.id}\n"
        f"И вообще {user.display_name} - душка! :3"
    )


@bot.command(aliases=["Повторяй", "повторяй", "повтори", "Повтори!"])
async def repeat(ctx, *, message):
    """Повторяет сообщение за пользователем"""
    await ctx.reply(f"{message}")


#!todo
# test command
@bot.command(aliases=["bite", "кусь"])
async def embedded(ctx, user: discord.Member = None):
    gif_list = [
        "https://images-ext-1.discordapp.net/external/PVj_uszl5XBEPL7CUnhHFV7AM_jDl34PeQMjtzCwQmQ/https/media.tenor.com/wyDB9guDGekAAAPo/nom-nom.mp4",
        "https://images-ext-1.discordapp.net/external/Xo-eUKAU0CjrCXUDRD8_E07PGq1MqJ5ZeQO1xv9dJ0s/https/media.tenor.com/_AkeqheWU-4AAAPo/anime-bite.mp4",
        "https://images-ext-1.discordapp.net/external/7rSDmWPj_SGcM5bI_IgBAqxUNJM2BqhDtkSwEUKGVTg/https/media.tenor.com/mXc2f5NeOpgAAAPo/no-blood-neck-bite.mp4",
        "https://tenor.com/view/nom-nom-gif-14060451299149945321",
    ]
    if not user:
        await ctx.send("Пожалуйста, упомяни пользователя, которого хочешь кусьнуть!")
        return
    color = int("FF81F6", 16)
    embed = discord.Embed(
        title="Кусь!",
        description=f"{ctx.author.mention} кусьнул(а) {user.mention}!",
        color=color,
    )
    embed.add_field(
        name="Что произошло?",
        value="Кусь - это акт любви! ❤️",
        inline=False,
    )
    embed.set_image(url=choice(gif_list))  # Ссылка на гифку
    embed.set_footer(text="Кусь-кусь!")

    await ctx.send(embed=embed)


# guilds


@bot.command(aliases=["Участники", "участники"])
async def members(ctx):
    """Показывает количество участников на сервере"""
    guild = ctx.guild
    await ctx.send(f"Количество участников на сервере: {guild.member_count}")


@bot.command(aliases=["расскажи о сервере"])
async def server_info(ctx):
    """Рассказывает о сервере"""
    guild = ctx.guild
    await ctx.reply(
        f"Мы попали на прекрасный сервер!\nИмя сервера: {guild.name}\nID сервера: {guild.id}\nПрикольный владелец: {guild.owner} :)"
    )

# channels

@bot.command(aliases=['Передай привет Динаре', "Передавай приветик Динарочке ^^"])
async def hello_to_Dinara(ctx):
    await ctx.send("Большой и пламенный привет от меня, Динара! А так же и от моего самого прекрасного разработчика, Яна ^^\nПо секрету... он тебя очень любит! Даже больше чем меня)\nМеня кормят и заботятся, поэтому переживать об о мне не стоит, рад с тобой познакомиться! :)")

@bot.command(aliases=["Канал", "каналы"])
async def channel(ctx):
    """Рассказывает о канале"""
    channel_name = ctx.channel.name
    await ctx.reply(f"Мы с вами находимся в канале: {channel_name}! Тут так уютно :D")

if __name__ == '__main__':
    bot.run(get_token())
