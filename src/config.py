import os

BASE_URL = "https://favqs.com/api"
API_KEY = os.getenv("FAVQS_API_KEY")
if not API_KEY:
    raise RuntimeError("FAVQS_API_KEY is not set")
