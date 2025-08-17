import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
script_path = ROOT_DIR / "triggers.sql"
db_path = ROOT_DIR / "reminderapp.db"

try:
    sqliteConnection = sqlite3.connect(str(db_path))
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    with open(str(script_path), "r") as sqlite_file:
        sql_script = sqlite_file.read()

    cursor.executescript(sql_script)
    sqliteConnection.commit()
    print("SQLite script executed successfully")
    cursor.close()

except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
