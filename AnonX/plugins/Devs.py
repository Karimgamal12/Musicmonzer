import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
@app.on_message(
    command(["صورص","سورس","السورس","افاتار", "افتار"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/38b8d6343df1d0aed46fa.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 
么  [𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒗𝒂𝒕𝒂𝒓♡](t.me/sourceav)
么 [𝑘𝑖𝑛𝑔](t.me/TR_E2S_ON_MY_MOoN) 
么 [َ𝒎𝒐𝒏𝒛𝒆𝒓](t.me/Z_X_Z_B) 
╰──── • ◈ • ────╯ 
  
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑘𝑖𝑛𝑔♡", url=f"https://t.me/TR_E2S_ON_MY_MOoN"), 
                ],[
                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒗𝒂𝒕𝒂𝒓 ♡", url=f"t.me/sourceav"),
                ],

            ]

        ),

    )
@app.on_message(
    command(["منزر","المبرمج منذر","منذر"])
)

@app.on_edited_message(command(["منزر","المبرمج منذر","منذر"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(5593884330)
  user = await client.get_chat(5593884330)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(5593884330,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 5593884330 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(5593884330, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
@app.on_message(
    command(["محمد","المبرمج كينج","كينج "])
)
@app.on_edited_message(command(["محمد","المبرمج كينج","كينج"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(1400467850)
  user = await client.get_chat(1400467850)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(1400467850,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 1400467850 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(1400467850, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
@app.on_message(
    command(["مولتو","المبرمج مولتو","المطور مولتو"])
)
@app.on_edited_message(command(["مولتو","المبرمج مولتو","المطور مولتو"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(21436464499494824894)
  user = await client.get_chat(2144664646469463824894)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(21438248646464646494,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 5593884330 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(214382464646464894, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                        
