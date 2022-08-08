from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili


ADMINS=['1282301807']
BOT_TOKEN='5396598765:AAGcyUdYGHWosR9bQJQVfQ86BIXoa2TVzJw'
ip='localhost'
CHANNELS=['-1001719663128']