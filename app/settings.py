from environs import Env

env = Env()

DEBUG = env.bool("DEBUG", False)
PORT = env.int("PORT", 9999)
TESTING = env.bool("TESTING", False)
MAX_LATENCY = env.int("MAX_LATENCY", 30)
DEFAULT_STATUS_CODE = env("DEFAULT_STATUS_CODE", 200)
