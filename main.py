import discord
import datetime
import os
import sys

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        lock()
        log(logfile, 'Logged on as', self.user)

    async def on_message(self, message):
        print(message.guild.id, message.channel.id, message.author.id, message.content)
        if self.noped(message):
            log(logfile, f'yeeting a message: {repr(message.content)}')
            await message.delete()
            await message.channel.send("nope")
    
    def noped(self, message):
        if (message.guild.id, message.channel.id, len(message.content)) == (1203529312016400435, 1228031264565497898, 3):
            return True
        #if message.content == 'nope':
        #    return True
        #if (message.guild.id, message.channel.id, message.author.id, len(message.content)) == (1203529312016400435, 1228031264565497898, 784682603336302634, 3):
        #    return True
        #if len(message.content) == 3 and message.content[0] == message.content[2] and message.content[0] != message.content[1]:
        #    return True
        #if '<@953758541666209852>' in message.content:
        #    return True
        return False

def log(f, *message):
    for part in message:
        if type(part) == str:
            f.write(part)
        else:
            f.write(str(part))
        f.write('\n')
        f.flush()
    print(*message)

def lock():
    global lockfile
    try:
        lockfile = open('.lock', 'r')
        sys.exit()
    except:
        lockfile = open('.lock', 'w')

def unlock():
    lockfile.close()
    os.remove('.lock')

logfilename = os.path.join('output', f'nope-log-{datetime.datetime.now()}.txt'.replace(':', '.'))
logfile = open(logfilename, 'w')

log(logfile, 'Starting...')

intents = discord.Intents.all()

with open("token", "r") as tokenfile:
    token = tokenfile.read()
log(logfile,'Read token')

client = MyClient(intents = intents)

log(logfile, "Initialized client")
client.run(token)
