"""
Coder : @MN19E
"""
A = " Coder : @MN19E"
import json
from pyrogram import Client, filters, idle
import asyncio
from pyromod import listen
try:
	open ("rd.json","r")
except:
	with open("rd.json","w") as f :
		f.write("{}")
api_id = 22276555 # Here Api Id 
api_hash = "108661230296aa7ccce3d27f57e168be" # Here Api Hash 
bot_token = "7075404703:AAF3C0WH51cfmwrzos2R1F2WiqIGg6efCgU" # Here Bot Token  
app = Client("iiu", api_id=api_id,api_hash=api_hash, bot_token=bot_token)
da = json.load(open("rd.json","r"))
def save(data):
	with open("rd.json","w",encoding='utf-8') as f:
		json.dump(data,f,indent=6,ensure_ascii=False)
		f.close()
def ck(c):
	try:
		da[c]
	except KeyError:
		da[c] = {}
		save(da)
@app.on_message(filters.regex("^اضف رد$"))
async def t(client, m):
	cid = str(m.chat.id)
	ck(cid)
	t = await m.chat.ask('• ارسل الان الكلمه لاضافتها في الردود', filters=filters.text & filters.user(m.from_user.id), reply_to_message_id=m.id)
	if t.text in da[cid]:
		await app.send_message(cid, "الرد مضاف من قبل !", reply_to_message_id=t.id)
	else:
		tt = await m.chat.ask("• حسناً يمكنك اضافة\n( نص,صوره,فيديو,متحركه,بصمه,اغنيه,ملف )", filters=filters.user(t.from_user.id), reply_to_message_id=t.id)
		if tt.text:
			da[cid][t.text] = f"text&{tt.text}"
			save(da)
			await tt.reply(f'• تم اضافه الرد بأسم ↤︎ ({t.text}) .', quote=True)
		elif tt.photo:
			da[cid][t.text] = f"photo&{tt.photo.file_id}"
			save(da)
			await tt.reply(f'• تم اضافه الرد بأسم ↤︎ ({t.text}) .', quote=True)
		elif tt.video:
			da[cid][t.text] = f"video&{tt.video.file_id}"
			save(da)
			await tt.reply(f'• تم اضافه الرد بأسم ↤︎ ({t.text}) .', quote=True)
		elif tt.animation:
			da[cid][t.text] = f"animation&{tt.animation.file_id}"
			save(da)
			await tt.reply(f'• تم اضافه الرد بأسم ↤︎ ({t.text}) .', quote=True)
		elif tt.voice:
			da[cid][t.text] = f"voice&{tt.voice.file_id}"
			save(da)
			await tt.reply(f'• تم اضافه الرد بأسم ↤︎ ({t.text}) .', quote=True)
		elif tt.audio:
			da[cid][t.text] = f"audio&{tt.audio.file_id}"
			save(da)
			await tt.reply(f'• تم اضافه الرد بأسم ↤︎ ({t.text}) .', quote=True)
		elif tt.document:
			da[cid][t.text] = f"document&{tt.document.file_id}"
			save(da)
			await tt.reply(f'• تم اضافه الرد بأسم ↤︎ ({t.text}) .', quote=True)
		else:
			await tt.reply(f"• تسطيع ارسال\n( نص,صوره,فيديو,متحركه,بصمه,اغنيه,ملف ) فقط !", quote=True)

@app.on_message(filters.regex("^الردود$"))
async def t(client, m):
	r = ""
	i = 0
	cid = str(m.chat.id)
	ck(cid)
	if da[cid] != {}:
		for a,b in da[cid].items():
			tp = b.split("&",1)
			if tp[0] == "text":
				t = "نص"
			elif tp[0] == "photo":
				t = "صوره "
			elif tp[0] == "video":
				t = "فيديو "
			elif tp[0] == "animation":
				t = "متحركه"
			elif tp[0] == "voice":
				t = "بصمه "
			elif tp[0] == "audio":
				t = "صوت"
			elif tp[0] == "document":
				t = "ملف"
			i += 1
			r += f'{i} => {a} ~ {t}\n'
		await m.reply(r)
	else:
		await m.reply("لا توجد ردود مضافة !")
@app.on_message(filters.regex("^مسح الردود$"))
async def t(client, m):
	cid = str(m.chat.id)
	ck(cid)
	if da[cid] != {}:
		da[cid] = {}
		save(da)
		await m.reply("تم حذف الردود.")
	else:
		await m.reply("لا توجد ردود مضافة !")
		
@app.on_message(filters.regex("^حذف رد$"))
async def t(client, m):
	cid = str(m.chat.id)
	ck(cid)
	t = await m.chat.ask('• ارسل الان الكلمه لحذفها من الردود', filters=filters.text & filters.user(m.from_user.id), reply_to_message_id=m.id)
	if t.text in da[cid]:
		da[cid].pop(t.text)
		save(da)
		await t.reply("تم حذف الرد.")
	else:
		await t.reply("الرد غير موجود بالفعل !")
@app.on_message(filters.text)
async def t(client, m):
	cid = str(m.chat.id)
	if cid in da:
		for a,b in da[cid].items():
			tp = b.split("&",1)
			if m.text == a:
				if tp[0] == "text":
					await m.reply(tp[1])
				elif tp[0] == "photo":
					await m.reply_photo(tp[1])
				elif tp[0] == "video":
					await m.reply_video(tp[1])
				elif tp[0] == "animation":
					await m.reply_animation(tp[1])
				elif tp[0] == "voice":
					await m.reply_voice(tp[1])
				elif tp[0] == "audio":
					await m.reply_audio(tp[1])
				elif tp[0] == "document":
					await m.reply_document(tp[1])
print ("#" * 25)
print (A.center(25,"#"))
print ("#" * 25)
print ("running ...")
app.start()
idle()
"""
Coder : @MN19E
"""