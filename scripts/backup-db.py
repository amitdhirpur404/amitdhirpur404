# Script to backup PostgreSQL database

import subprocess
import datetime

today = datetime.date.today()
filename = f"backup_{today}.sql"

try:
    subprocess.run([
        "pg_dump", "-U", "postgres", "mydb", "-f", filename
    ], check=True)
    print(f"Database backup saved as {filename}")
except subprocess.CalledProcessError as e:
    print("Error during backup:", e)
