import os


BOT_TOKEN = ''
admins = [
    1099391285,  # Никита
    868136575  # Кирилл
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
