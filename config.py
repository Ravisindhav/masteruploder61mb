import os

API_ID = API_ID = 20831039

API_HASH = os.environ.get("API_HASH", "ea20b722f7af827db12fb85f4d55238c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7798912189:AAE8JGVI_yZBVnAZoMwehyooksKlUPL1M8s")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5170349400))

LOG = -1002146213576

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5170349400").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
