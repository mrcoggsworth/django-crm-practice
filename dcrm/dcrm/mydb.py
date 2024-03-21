"""_summary_
"""

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv(key="DATABASE_HOST")
USER = os.getenv(key="DATABASE_USER")
PASSWORD = os.getenv(key="DATABASE_PASSWORD")

# print(HOST, USER, PASSWORD)

db = mysql.connector.connect(host=HOST, user=USER, passwd=PASSWORD)

cursorObject = db.cursor()
cursorObject.execute("SHOW DATABASES")
print("DONE")
