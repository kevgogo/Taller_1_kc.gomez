from dotenv import load_dotenv
import os

load_dotenv()

print(f"APP_ENV: {os.getenv('APP_ENV')}")
print(f"ENABLE_PRINTS: {os.getenv('ENABLE_PRINTS')}")
print(f"ENCRYPT_PASSWORDS: {os.getenv('ENCRYPT_PASSWORDS')}")
print(f"DB_TYPE: {os.getenv('DB_TYPE')}")
print(f"MYSQL_USER: {os.getenv('MYSQL_USER')}")
print(f"MYSQL_PASSWORD: {os.getenv('MYSQL_PASSWORD')}")
print(f"MYSQL_HOST: {os.getenv('MYSQL_HOST')}")
print(f"MYSQL_PORT: {os.getenv('MYSQL_PORT')}")
print(f"MYSQL_DB: {os.getenv('MYSQL_DB')}")

import secrets

secret_key = secrets.token_hex(32)
print(secret_key)
