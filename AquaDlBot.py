from pyrogram import Client , filters
import wget
import os
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup


#Developed by @AsiaXDev
#repo -> https://github.com/AsiaXDev/AquaDlBot

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

nezuko = Client(
    "my_bot",
    bot_token="BOT_TOKEN",
    api_id="API_ID",
    api_hash="API_HASH"
    
)


gif = f"/home/raveen/Downloads/Aqua.gif"

cap_text =  ''' <b>Hello senpai!</b> 
            <b> \n\n!! Im Aqua an URl UPLOADER BOT !! </b> 
            <b> \n\n !! ytdl links not supported right now !! </b> 
            <b> \n\n !! Currently supports upto 2gb! IF YOU AB(USE) ILL DIE🥺! </b>
            '''               

@nezuko.on_message(filters.command(["start"]))
async def start (client , message):
    chat_id = message.chat.id
    await nezuko.send_animation(chat_id ,gif , caption= cap_text )



def progress(current, total):
        print(f"{current * 100 / total:.1f}%") 

thumbpic= f"/home/raveen/Downloads/aquadl.jpg"

@nezuko.on_message(filters.command(["dl"]))
async def download (client , message):
    await message.reply_text(text = f"**Got link.. Downloading 🥺")
    url = message.reply_to_message.text
    disable_web_page_preview = True
    filename = wget.download(url)  
    chat_id = message.chat.id
    await nezuko.send_document(chat_id ,filename , caption="uploaded with ❤️ by @AquaDLBot" , progress=progress , thumb=thumbpic)
    await message.reply_text(text = f"**Uploaded Successfully! 🥺")
    os.remove(filename)
    

#Developed by @AsiaXDev
#repo -> https://github.com/AsiaXDev/AquaDlBot


@nezuko.on_message(filters.command(["about"]))
async def about (client , message):
    keyboard = [
        [
            InlineKeyboardButton("JOIN",
                                          url="https://t.me/TheOstrich"),
            InlineKeyboardButton("SHARE",url="https://t.me/share/url?url=https://t.me/AquaDlBot")
        ],
    ]
    await message.reply_text(text =
                              "<b>Hey! My name is Aqua.</b>"
                              "\nI can Download and Upload Files for You senpai."
                              "\n\n<b>About Me :</b>"
                              "\n\n  - <b>Name</b>        : <a href=\"https://t.me/raveen2003/\">AQUA</a>"
                              "\n\n  - <b>Creator</b>      : <a href=\"https://t.me/AsiaxDev/\">Asia Argento</a>"
                              "\n\n  - <b>Language</b>  : <a href=\"https://www.python.org/\">Python 3</a>"
                              "\n\n  - <b>Library</b>       : <a href=\"https://docs.pyrogram.org//\">PYROGRAM</a>"
                              "\n\n  - <b>Source Code</b>  : <a href=\"https://github.com/AsiaxDEv/AquaDLBot\">Source Code</a>",    
        disable_web_page_preview = True ,
        reply_markup = InlineKeyboardMarkup(keyboard)
     )


#Developed by @AsiaXDev
#repo -> https://github.com/AsiaXDev/AquaDlBot        



@nezuko.on_message(filters.command(["help"]))
async def help (client , message):
    await message.reply_text(text = "<b> Need help ? </b>"
                                    "<b> \n\n I can help you download files less than 2GB </b>"
                                    "<b> \n\n Just send me a link and reply it with /dl </b>"
                                    "<b> \n\n To know More About me &  to get Source Code /about </b>"
                                    "<b> \n\n /support to get support </b>"
                                    "<b> \n\n /donate to donate this bot !</b>")

@nezuko.on_message(filters.command(["support"]))
async def support(client , message):
    await message.reply_text(text = "<b> currently there is no support for this bot🥺! </b>"
                                    "<b> \n\n JOIN @TheOstrich !</b>")

#when donating me 🥺
@nezuko.on_message(filters.command(["donate"]))
async def donate(client , message):
    keyboard = [
        [
            InlineKeyboardButton("Contribute",
                                          url="https://github.com/AsiaXDev"),
            InlineKeyboardButton("UPI",url="https://upayi.me/raveen-2003@axl"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text("Thank you for comming forwad to donate" , reply_markup=reply_markup)



#Developed by @AsiaXDev
#repo -> https://github.com/AsiaXDev/AquaDlBot



        
nezuko.run()
#Developed by @AsiaXDev
#repo -> https://github.com/AsiaXDev/AquaDlBot