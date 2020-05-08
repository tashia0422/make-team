import os
import traceback

import discord
from discord.ext import commands

from modules.grouping import MakeTeam

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')

"""起動処理"""
@bot.event
async def on_ready():
    print('-----Logged in info-----')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------------------------')

"""コマンド実行"""
# メンバー数が均等になるチーム分け
@bot.command()
async def team(ctx, specified_num=2):
    make_team = MakeTeam()
    remainder_flag = 'true'
    msg = make_team.make_party_num(ctx,specified_num,remainder_flag)
    await ctx.channel.send(msg)

# メンバー数が均等にはならないチーム分け
@bot.command()
async def team_norem(ctx, specified_num=2):
    make_team = MakeTeam()
    msg = make_team.make_party_num(ctx,specified_num)
    await ctx.channel.send(msg)

# メンバー数を指定してチーム分け
@bot.command()
async def group(ctx, specified_num=1):
    make_team = MakeTeam()
    msg = make_team.make_specified_len(ctx,specified_num)
    await ctx.channel.send(msg)
 # ヘルプ   
@bot.command()
async def ping(ctx):
    await ctx.send('  
                   /team [チーム数]
                    指定した数のチームを作成
                    メンバー数が同じになるように作成
                    チーム数を指定しなくても実行可。デフォルトで"2"を指定
                    /team_norem [チーム数]
                     指定した数のチームを作成
                     人数差は考慮されないまま、指定されたチーム数を作成
                    チーム数を指定しなくても実行可。デフォルトで"2"を指定
                    /group [メンバー数]
                    指定したメンバー数でチームを作成
                    メンバー数を指定しない場合、デフォルトとして"1"を指定
                   ')  
   

"""botの接続と起動"""
bot.run(token)
