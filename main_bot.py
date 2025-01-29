from discord import Interaction
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
from dotenv import load_dotenv
import os
import asyncio
from random import choice

"""Это дискорд бот"""


def get_token():
    load_dotenv()
    BOT_TOKEN = os.getenv("SECRET_TOKEN")
    return BOT_TOKEN


intents = discord.Intents.default()
intents.message_content = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Бот: {bot.user}, готов к работе!")


@bot.command(aliases=["Привет!", "привет", "Привет", "Hello", "hello!", "Hello!"])
async def hello(ctx):
    """Приветствует пользователя"""
    author = ctx.author.display_name
    await ctx.reply(f"Приветик, {author}!")


@bot.command(aliases=["Расскажи о создателе", "создатель", "who_is_the_creator"])
async def tell(ctx, *, message):
    """Рассказывает о создателе"""
    if (
        message == "Расскажи о создателе".lower()
        or message == "who_is_the_creator"
        or message == "создатель"
    ):
        await ctx.reply(
            f"Моим создателем и героем является... *звук барабанных палок*... Облачко! а точнее - @doesitreal!"
        )
    if message == "хм".lower():
        await ctx.reply("Что-то не так?")


#! timer
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
        "https://media1.tenor.com/m/5mVQ3ffWUTgAAAAd/anime-bite.gif",
        "https://media1.tenor.com/m/mXc2f5NeOpgAAAAd/no-blood-neck-bite.gif",
        "https://media1.tenor.com/m/_AkeqheWU-4AAAAd/anime-bite.gif",
        "https://media1.tenor.com/m/n0DPyBDtZHgAAAAd/anime-bite.gif",
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


@bot.command(aliases=["Канал", "каналы"])
async def channel(ctx):
    """Рассказывает о канале"""
    channel_name = ctx.channel.name
    await ctx.reply(f"Мы с вами находимся в канале: {channel_name}! Тут так уютно :D")


bot.run(get_token())
