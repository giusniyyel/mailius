#  Copyright (c) 2025 Giusniyyel
#
#  This source code is licensed. For terms of use, redistribution, and contributions,
#  please visit: https://giusniyyel.dev/software/license
from dotenv import load_dotenv
import os

load_dotenv()

PRODUCT_NAME = os.getenv("PRODUCT_NAME")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
MAILGUN_BASE_URL = os.getenv("MAILGUN_BASE_URL")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECIPIENT_EMAILS = os.getenv("RECIPIENT_EMAILS")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
AFFIRMATION_API_URL = os.getenv("AFFIRMATION_API_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")