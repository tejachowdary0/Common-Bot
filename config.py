import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # star bots client config
    API_ID    = os.environ.get("API_ID", "27604683")
    API_HASH  = os.environ.get("API_HASH", "ed52a1d0803b2ed84c5cca7f20535aac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6636903897:AAH4jTAphNyRH9jHXQfi-FQd3WO-3LSRcxU") 
   
    # database config
    DATABASE_NAME = os.environ.get("DATABASE_NAME","rename") # Bot Username  
    DATABASE_URL  = os.environ.get("DATABASE_URL","mongodb+srv://tejachowdary106:6VZqrpK9PxLQXOS6@hotstar.fpazw92.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    PIC         = os.environ.get("PIC", "https://graph.org/file/1412d9f93d77c350d8268.jpg")
    ADMINS      = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1264280791').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001910675865"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))

class Text(object):
    # part of text configuration
    START_TEXT = """<b>Hello 👋🏻 {} ❤️,\nI'm An Star Bots Tamil's Official () Bot. This is An Advanced () Bot.\n➠ For More Details Check /help\n\nMaintenance By :- [Star Bots Tamil](https://t.me/Star_Bots_Tamil)</b>"""

    ABOUT_TEXT = """<b>🤖 My Name :- {}\n
🧑🏻‍💻 Developer :- <a href=https://t.me/TG_Karthik><b>Karthik</b></a>\n
💁🏻 My Best Friend :- {}\n
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
➠ /stats :- Total Users 📊
➠ /ban :- Ban a User 🚫
➠ /unban :- Unban a User 😁
➠ /banned :- Total Banned Users 🤕
➠ /broadcast :- to Broadcast 💌 a Message to All Users

⚠️ Contact For Any Problem :- [👥 Support Group](https://t.me/Star_Bots_Tamil_Support)</b>"""

    DEV_TXT = """<b><u>Special Thanks & Developer</b></u>
**You Can pay Any Our Bot's Repo. If you're able to Donate or Buy Our Bot's Repo, please Consider using these Methods:

UPI ID :- `starbotstamil@upi`

GPay :- `starbotstamil@oksbi`

Phonepe :- `starbotstamil@ybl`

Paytm :- `starbotstamil@paytm`

After pay Must Send Screenshot Admin**

<b>🧑🏻‍💻 Developer :- </b><a href=https://t.me/TG_Karthik><b>Karthik</b></a>
**Contact me for more info**"""
