from environs import Env

env = Env()

DEBUG = env.bool('DEBUG', False)
PORT = env.int('PORT', 9999)
TESTING = env.bool('TESTING', False)

