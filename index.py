import os
import discord
from discord.ext import commands
from discord.ext.commands import Option
from flask import render_template, Flask
app = Flask(__name__, template_folder='templates')


import g4f
from g4f.Provider import (
    AItianhu,
    Aichat,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    OpenaiChat,
    Vercel,
    You,
    Yqcloud,
)

pt1 = 'MTE2NjUzOTIwMDA2NjIzNjQ2Ng'
pt2 = '.G3qs9w.'
pt3 = 'IiUUYnfi9F0aRpAuz_RGT_M-QmF2OnmPOf0fkQ'
# Load your API key from an environment variable or secret management service

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(intents=intents)

@app.route('/')
def index():
    return "Running"
@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}, {bot.user.id}, ping is {bot.latency}ms')
	print(bot.user.name)
	print(bot.user.id)

@bot.slash_command(name='text', description='Generate text using your prompt')
async def text(ctx, prompt: Option(str, "Enter your prompt", required = True, default = '')):
	await ctx.respond(f'<@!{ctx.author.id}>, Generating from prompt: {prompt}', delete_after = 2)
	def generate_prompt():
		return f"""{prompt}"""
	if 1==1:
		response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    provider=Bing,
    messages=[{"role": "user", "content": generate_prompt()}],
)  # altern
		final = response.strip('Using Bing Provider')
		if "code" in prompt:
			message =  await ctx.send('Generating...')
			print('No errors')
			await message.edit(f"""<@!{ctx.author.id}>```
	    {final}
	```""")
			print(bot.latency)
		elif "code" not in prompt:
			message = await ctx.send('Generating...')
			print('No errors')
			await message.edit(f"<@!{ctx.author.id}>{final}")
			print(bot.latency)  

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)

bot.run(pt1+pt2+pt3)
