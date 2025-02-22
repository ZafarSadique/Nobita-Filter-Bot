import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/zsbhere')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Dasdb2:dasdb12345@cluster0.5evyh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://Test:test12345@cluster0.4bomw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', ''))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/wam.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002194850073').split()]
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "-1001779351808, -1002486191880")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', ''))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', ''))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/how_to_dwnload/31")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/how_to_dwnload/37")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/how_to_dwnload/22")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "6caa2252957519f1874398b83bb5532d0b0c56de")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "Shortyfi.link")
SHORTENER_API2 = environ.get("SHORTENER_API2", "46ac5441b1b2e3c7d770715b42bf8c8160c7c947")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "adcash.in")
SHORTENER_API3 = environ.get("SHORTENER_API3", "826eb92e893f6fdb42920983bba04c409bdc0b5d")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "tnshort.net")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "120"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "120"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', ''))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', True)
