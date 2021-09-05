from javascript import require, On, Once, AsyncTask, once, off
import time
import os

#information on server and bot
mineflayer = require('mineflayer')
BOT_USERNAME="spy"
bot = mineflayer.createBot({ 'host': 'shield.1b1t.me', 'port': 25565, 'username': BOT_USERNAME, 'hideErrors': False })
password =
Login = False
@On(bot, 'chat',)
def onChat(this, user, message, task, *rest):
           
        
	#login and chat log, login requied on some server custom password are recomended 
	if '/register' in message:
		bot.chat('/register'+ password + password)
	if '/login' in message:
		Login = True
		bot.chat('/login' + password)
		time.sleep(2)
		Login = False
		 
	if '%stop' in message:
		bot.chat('stopping bot, spy')
		bot.quit()


	@AsyncTask(start=True)
	def break_block(task):
		for x in range(100):
		
			bot.chat('/tpy wullie')
			time.sleep(5)
			bot.chat('/tpy chmoka90')
			time.sleep(5)
			bot.chat('/tpy RealSteak')
		
			bot.chat('/tpy Mr_Trebor')
		
			bot.chat('/tpy _Smertushka_')
			
			bot.chat('/tpy MulfoK')
		    
			bot.chat('/tpy jaya_97')
			
			bot.chat('/tpy jqjj')
			
			bot.chat('/tpy SpyrowGr')
			time.sleep(2)				
		
		
