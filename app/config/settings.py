import os

class Settings:
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")
    # DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///app.db")
