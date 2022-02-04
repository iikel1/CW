import discord
from discord.ext import commands
import re
import longr as long

client = commands.Bot(command_prefix='rb!')

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    msg_cer = 0
    hrwords = True
    

    for word in user_message:
        if word in recognised_words:
            msg_cer += 1

    percentage = float(msg_cer) / float(len(recognised_words))

    for word in recognised_words:
        if word not in user_message :
            has_required_words = False
            break
    
    if has_required_words or single_response :
        return int(percentage*100)
    else :
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


async def get_response(channel, user_input):
    spilt_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(spilt_message)
    Ch1 = client.get_channel(channel)
    return await Ch1.send(response) 





@client.event
async def on_ready():
    print("online ")



@client.event
async def on_message(message):
    if message.channel.id == 938836127404675072 :
        channel = 938836127404675072
        if message.author.id == 889824977803673632 :
            return
        
        
        def pred(m):
                return m.author == message.author and m.channel == message.channel
        answer1 = await client.wait_for("message", check=pred)
        await get_response(channel, answer1.content)
        
            
    await client.process_commands(message) 


client.run("ODg5ODI0OTc3ODAzNjczNjMy.YUm4Fg.uT2Gp0AdjU1CG9thr1NdOlO-0k8")