import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # star bots client config
    API_ID    = os.environ.get("API_ID", "11973721")
    API_HASH  = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DATABASE_NAME = os.environ.get("DATABASE_NAME","") # Bot Username  
    DATABASE_URL  = os.environ.get("DATABASE_URL","mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    PIC         = os.environ.get("PIC", "https://graph.org/file/1412d9f93d77c350d8268.jpg")
    ADMINS      = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1391556668 5162208212 5239847373').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Star_Bots_Tamil") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))

class Text(object):
    # part of text configuration
    START_TEXT = """<b>Hello 👋🏻 {} ❤️,\nI'm An Star Bots Tamil's Official Rename Bot. This is An Advanced and Yet Powerful Rename Bot.\nFor More Details Check /help\n\n➠ You Can Rename File / Video.\n➠ Change Thumbnail of Your File / Video.\n➠ Convert Video to File & File to Video.\nOur Bot Fully customisable\n➠ Permanent Thumbnail 🖼️ and Custom Caption ✍🏻.\n\nMaintenance By :- [Star Bots Tamil](https://t.me/Star_Bots_Tamil)</b>"""

    ABOUT_TEXT = """<b>🤖 My Name :- {}\n
🧑🏻‍💻 Developer :- <a href=https://t.me/TG_Karthik><b>Karthik</b></a>\n
📝 Language :- Python3\n
📚 Framework :- Pyrogram\n
📡 Hosted on :- VPS\n
💾 Database :- <a href=https://cloud.mongodb.com/>Mongo DB</a>\n
🎥 Movie Updates :- <a href=https://t.me/Star_Moviess_Tamil><b></b>Star Movies Tamil</a>\n
🤖 Bot Channel :- <a href=https://t.me/Star_Bots_Tamil><b></b>Star Bots Tamil</a></b>"""

    HELP_TEXT = """
<b><u>Available Commands</u>

➠ /start :- Check if 😊 I'm Alive
➠ /help :- How to Use❓
➠ /about :- to Know About Me 😌
    
🖼️ <u>How to Set Thumbnail</u>
 
➠ /start The Our Bot And Send Any Photo to Automatically Set Thumbnail 🖼️
➠ /showthumbnail :- View Current Thumbnail 🖼️
➠ /deletethumbnail :- Delete 🗑️ Your Thumbnail 🖼️

✍🏻 <u>How to Set Custom Caption</u>

➠ /set_caption :- Set Custom Caption ✍🏻
➠ /see_caption :- View Current Caption ✍🏻
➠ /del_caption :- Delete 🗑️ Your Caption
Example :- `/set_caption 📁 File Name :- {filename}

💾 File Size :- {filesize}

⏰ Duration :- {duration}`

✏️ <u>How to Rename File</u>

➠ Send me Any File And Type New File Name

<u>📂 Supported File Formats</u>

➠ 📁 Document
➠ 🎥 Video
➠ 🎵 Audio

⚠️ Contact For Any Problem :- [👥 Support Group](https://t.me/Star_Bots_Tamil_Support)</b>"""

    DEV_TEXT = """<b><u>Special Thanks & Developer</b></u>
<b>🧑🏻‍💻 Developer :- </b><a href=https://t.me/TG_Karthik><b>Karthik</b></a>"""
