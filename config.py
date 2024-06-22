# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29698312")

API_HASH = os.environ.get("API_HASH", "c8792f673ecdff8e99f3da111ac0f6f5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6436829140:AAG5cCVSu--K7eh5gllKoKu1D7looBa9QQQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Gurjitnagra13bot") 

             # Don't Remove Credit @Gurjitnagra13bot
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Gurjitnagra13bot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://gurinagra77:AacV0qRaSjcN89Fs@cluster0.mqst7yk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '850672171').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @gurjit_nagra13
# Subscribe YouTube Channel For Amazing Bot @gurjit_nagra13
# Ask Doubt on telegram @KingVJ01
