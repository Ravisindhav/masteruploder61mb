import os

API_ID = API_ID = 27660379

API_HASH = os.environ.get("API_HASH", "19c71c27733f0954371085198855125a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7971998323:AAHTuNTLIL5PaQElqpLMhiun8axj1ucFsDY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5459854363))

LOG = -1002761572365

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5459854363").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
