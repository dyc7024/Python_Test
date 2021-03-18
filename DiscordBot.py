import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("--- 연결 성공 ---")
    print(f"봇 이름: {bot.user.name}")
    print(f"ID: {bot.user.id}")
    await bot.change_presence(activity=discord.Game("당신과 함께"))


@bot.command()
async def hi(ctx):
    await ctx.send("Hello!")

@bot.command()
async def made(ctx):
    embed = discord.Embed(description="보고 배운곳", color=0xA1FF8E, timestamp=ctx.message.created_at)
    embed.set_author(name="디시인사이드 디스코드 갤러리", url="https://gall.dcinside.com/mgallery/board/lists?id=discord")
    embed.set_thumbnail(url="https://d1nxzqpcg2bym0.cloudfront.net/google_play/com.dcinside.app/2f7464ce-b4ab-11ea-9c74-6fb55c2c2087/128x128")
    await ctx.send(embed=embed)


bot.run("YourBotToken")
