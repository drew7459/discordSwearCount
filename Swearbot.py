'''
Mung Bot
Drew Patel May 29, 2020
'''

## Initialization ## 
import pickle
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
swearEnabled = True

#Swear List
swearList = ['ass','bitch','cbt','cunt',
'damn','fag','fuck','gay','hell','mung',
'nigger','shit','slut','wtf']

swearDictFile = "data.txt"

def swearCount(user, word):
    if(user == 'MungBot#1353'):
        return True
    if(word in swearList):
        val = swearList.index(word)
        if user in swearDict:
            swearDict[user][val] += 1
            saveData()
            return True
        else:
            swearDict[user] = [0]*len(swearList)
            swearDict[user][val] += 1
            saveData()
            return True
    else: 
        return False

def gatherTotal(user):
    total = 0
    if user in swearDict:
        for i in range(len(swearDict[user])):
            total += swearDict[user][i]
    return total

def gatherAdvancedData(user):
    if user is None:
        return "Please input user id, !d test#1234"
    if user in swearDict:
        details = "User: {}\nTotal: {}\n".format(user,gatherTotal(user))
        for i in range(len(swearList)):
            details += "\n{}: {}".format(swearList[i],swearDict[user][i])
        return details
    else:
        return "\nThis user has not cursed yet or is not found"

def getAllTotals():
    total = 0
    data = ""
    users = swearDict.keys()
    for user in users:
        total += gatherTotal(user)
        data += "\n{}: {}".format(user, gatherTotal(user))
    txt = "Total: {}\n".format(total) + data
    return txt

def loadData():
    if os.path.getsize(swearDictFile) > 0: 
        with open(swearDictFile,'rb') as file:
            swearDict = pickle.load(file)
        file.close()
    else: 
        swearDict = {}
    return swearDict

def saveData():
    with open(swearDictFile,'wb') as file:
        pickle.dump(swearDict, file)
    file.close()

def getTotalOfWord(user,word):
    if(word in swearList):
        val = swearList.index(word)
        if(user in swearDict):
            return swearDict[user][val]
    else:
        return -1

def swearCountMultiple(user, message):
    swear = False
    for word in swearList:
        if word in message:
            if(swear):
                swearCount(user,word)
            else:
                swear = swearCount(user,word)
    return swear

def toggle():
    global swearEnabled 
    swearEnabled = not swearEnabled
    return swearEnabled

swearDict = loadData()
print(swearDict)

## Commands ##

@bot.command(name='t', help='!t - toggles swear removal')
@commands.has_role('admin')
async def toggleSwearEnable(ctx):
    await ctx.send(toggle())

@bot.command(name='ut', help='!ut - Gives current swear count of all users')
async def total(ctx):
    await ctx.send(getAllTotals())

@bot.command(name='d', help='!d Test#1234 - Gives detailed account of words for a specific user')
async def details(ctx, name):
    await ctx.send(gatherAdvancedData(str(name)))

@bot.command(name='me', help='!me - Gives detailed account of words for you')
async def userTotal(ctx):
    await ctx.send(gatherAdvancedData(str(ctx.author)))

@bot.command(name='m', help='!m - mung')
async def mung(ctx):
    await ctx.send("mung")

@bot.command(name='c', help='!c - counts')
async def mung(ctx):
    await ctx.send()
## Events ##

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    global swearEnabled
    if swearCountMultiple(str(message.author), str(message.content.lower())):
        if(swearEnabled):
            await message.channel.send("{}, your message has been censored.".format(message.author.mention))
            await message.delete()

    await bot.process_commands(message)

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'{time.strftime("%H:%M:%S", time.localtime())}- Unhandled message: {args[0]}\n')
        else:
            raise

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)