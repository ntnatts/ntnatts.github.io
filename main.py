import os
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")
db_url = os.getenv("DATABASE_URL")

print(f"API Key: {api_key}")
print(f"Database URL: {db_url}")
