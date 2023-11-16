import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "12227067")
API_HASH = os.getenv("API_HASH", "b463bedd791aa733ae2297e6520302fe")
BOT_TOKEN = os.getenv("BOT_TOKEN", "5894209648:AAF1waPORM1VIJ_J7XSTywlVf7JOoKOoBIU")
SUDOERS = list(map(int, os.getenv("SUDOERS", "6204761408").split()))
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.pom3ops.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", "-1001817662435")
MUST_JOIN = os.getenv("MUST_JOIN", "AMBOTYT")
DISABLED = list(map(int, os.getenv("DISABLED", "").split()))

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
