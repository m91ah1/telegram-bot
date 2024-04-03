import os
os.system("pip install pyrogram && pip install tgcrypto && pip install pyromod && clear")
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, idle
from pyromod import listen
from pyrogram.enums import ParseMode, ChatMemberStatus 

TOKEN = input ("Enter BOT TOKEN :\n-: ")
app = Client(
  "MY_L444Q", 13817616, "118fb0f2bfc0a7a54d1899c412e62a46",
  bot_token=TOKEN
  )
  
LOG = -1001366197783

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("l444q.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}𝚀444𝚇")[1].replace("\n",""))
    return False


def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("l444q.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}𝚀444𝚇{rd}\n")
    return True


def del_rd(x):
   word = str(x).replace("\n","")
   with open("l444q.txt", "r+") as fp:
      lines = fp.readlines()
   with open("l444q.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return



def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("l444q.txt").read()
    if chat_id not in gps:
      return False
    with open("l444q.txt", "r+") as fp:
      lines = fp.readlines()
    with open("l444q.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return


def get_rdod(chat_id):
   with open("l444q.txt", "r+") as f:
       lines = f.readlines()
   text = "• الردود بهذه المجموعة : \n"
   for line in lines:
     if str(chat_id) in line:
       a = line.split("#")[1]
       b = a.split("𝚀444𝚇")[0]
       text += f"{b}\n"
   if text == "• الردود بهذه المجموعة : \n": return False
   else: return f"**{text}**"
       
async def get_rtba(chat_id: int, user_id: int) -> bool:
    get = await app.get_chat_member(chat_id, user_id)
    if not get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      return False
    else: return True
    


@app.on_message(filters.regex("^اضف رد$") & filters.group)
async def adf_rd(app,message):
    get = get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
              )
    ask1 = await app.ask(
    message.chat.id, "ارسل كلمة الرد", reply_to_message_id=message.id, filters=filters.text & filters.user(message.from_user.id),reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
              )
    text = ask1.text
    ask2 = await app.ask(
    message.chat.id, "ارسل جواب الرد", reply_to_message_id=ask1.id, filters=filters.user(message.from_user.id),reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
              )
    copy = await ask2.copy(LOG)
    rd = copy.id
    a = add_rd(text, message.chat.id, rd)
    if a: return await ask2.reply("تم اضافة الرد بنجاح",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
)
    else: return await ask2.reply("حدث خطأ",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
              )


@app.on_message(filters.regex("^مسح رد$") & filters.group)
async def delete_rd(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   ask = await app.ask(
     message.chat.id, "ارسل الرد الآن", filters=filters.text & filters.user(message.from_user.id), reply_to_message_id=message.id)
   a = get_rd(ask.text, message.chat.id)
   if not a:
     return await ask.reply("الرد غير موجود",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
              )
   x = f"{message.chat.id}#{ask.text}𝚀444𝚇{a}"
   b = del_rd(x)
   await ask.reply("• تم مسح الرد",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
)


@app.on_message(filters.regex("^مسح الردود$") & filters.group)
async def delrdood(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
              )
   a = del_rdod(message.chat.id)
   print(a)
   if not a : return await message.reply("• تم مسح الردود هنا",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
             )
   else: return await message.reply("• لاتوجد ردود هنا",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
          )

@app.on_message(filters.regex("^الردود$") & filters.group)
async def get_rdodd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
               )
    a = get_rdod(message.chat.id)
    if not a: return await message.reply("• لا توجد ردود هنا",reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "♡{آلَصِـمِـتُ آجَـمِـلَ}♡", url=f"https://t.me/q444x"), 
                        ], 
                  ] 
               ), 
           )
    else: return await message.reply(a)


@app.on_message(filters.text & filters.group, group=1)
async def gettt_rd(app, message):
   a = get_rd(message.text, message.chat.id)
   if a: return await app.copy_message(message.chat.id, LOG, a, reply_to_message_id=message.id)
   else: return 
   
   
app.start()
print("- Done Upload Telegram Bot .\n- Can You Used Bot Now!")
idle()


