import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FACEBOOK_APP_ID = os.getenv('IPN_LUNCH_FACEBOOK_APP_ID')
    FACEBOOK_APP_SECRET = os.getenv('IPN_LUNCH_FACEBOOK_APP_SECRET')
    FACEBOOK_PAGE_ID = 'ipnbarcafetaria'
