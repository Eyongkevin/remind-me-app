import json
import sqlite3
from datetime import date, time
from pathlib import Path

db_path = Path("reminderapp.db")


# Save reminder data
def save_reminder(
    label: str,
    days: str,
    alert_type: str,
    alert_time: str,
    repeat: bool = False,
    active: bool = True,
):
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        query = """
            INSERT INTO reminder (label, days, alert_type, alert_time, active, repeat)
            VALUES(?, ?, ?, ?, ?, ?);
        """

        cursor.execute(query, (label, days, alert_type, alert_time, active, repeat))
        conn.commit()
        print("SQLite query executed successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def update_reminder(
    id: int,
    label: str,
    days: str,
    alert_type: str,
    alert_time: str,
    repeat: bool = False,
    active: bool = True,
):
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        query = """
            UPDATE reminder SET 
                label = ?,
                days = ?,
                alert_type = ?,
                alert_time = ?, 
                active = ?,
                repeat = ?
            WHERE id = ?;
        """

        cursor.execute(query, (label, days, alert_type, alert_time, active, repeat, id))
        conn.commit()
        print("SQLite query executed successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def delete_reminder(id: int):
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        query = """
            DELETE FROM reminder
            WHERE id = ?;
        """

        cursor.execute(query, (id,))
        conn.commit()
        print("SQLite query executed successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def toogle_state(id: int, active: bool):
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        query = """
            UPDATE reminder SET
                active = ?
            WHERE id = ?;
        """

        cursor.execute(
            query,
            (
                active,
                id,
            ),
        )
        conn.commit()
        print("SQLite query executed successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def fetch_all_reminders():
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        query = """
            SELECT * FROM reminder ORDER BY alert_time;
        """

        cursor.execute(query)
        reminders = cursor.fetchall()
        print("SQLite query executed successfully")
        cursor.close()
        return reminders

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def fetch_today_reminders():
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        day_abbr = f"%{date.today().ctime().split()[0]}%"  # LIKE %Sun%

        query = """
            SELECT * FROM reminder WHERE days LIKE ?;
        """

        cursor.execute(query, (day_abbr,))
        reminders = cursor.fetchall()
        print("SQLite query executed successfully")
        cursor.close()
        return reminders

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def fetch_by_day(day: str):
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        day = f"%{day}%"

        query = """
            SELECT * FROM reminder WHERE days LIKE ?;
        """

        cursor.execute(query, (day,))
        reminders = cursor.fetchall()
        print("SQLite query executed successfully")
        cursor.close()
        return reminders

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def fetch_by_active(active: bool):
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        query = """
            SELECT * FROM reminder WHERE active = ?;
        """

        cursor.execute(query, (active,))
        reminders = cursor.fetchall()
        print("SQLite query executed successfully")
        cursor.close()
        return reminders

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def fetch_by_state(state):
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        day_abbr = f"%{date.today().ctime().split()[0]}%"

        if state == "Passed":
            query = """
                SELECT * FROM reminder WHERE days LIKE ? AND alert_time < TIME(CURRENT_TIMESTAMP);
            """
            cursor.execute(query, (day_abbr,))
        else:
            query = """
                SELECT * FROM reminder WHERE 
                    (days LIKE ? AND alert_time > TIME(CURRENT_TIMESTAMP)) OR 
                    (days NOT LIKE ?);
            """
            cursor.execute(query, (day_abbr, day_abbr))

        reminders = cursor.fetchall()
        print("SQLite query executed successfully")
        cursor.close()
        return reminders

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def search_by_label(label: str):
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        label = f"%{label}%"
        query = """
            SELECT * FROM reminder WHERE label LIKE ?;
        """

        cursor.execute(query, (label,))
        reminders = cursor.fetchall()
        print("SQLite query executed successfully")
        cursor.close()
        return reminders

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def fetch_up_coming_reminder():
    # Get todays reminders that hasn't passed
    # Or get the next day's reminder
    # Fetch all active reminders and filter in Python
    active = 1
    return fetch_by_active(active)


def delete_all():
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        query = """
            DELETE FROM reminder;
        """

        cursor.execute(query)
        conn.commit()
        print("SQLite query executed successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


if __name__ == "__main__":

    #  Save reminder data
    # label = "Prepare for church"
    # days = ("Sun",)
    # alert_type = {"sound": True, "popup": False}
    # alert_time = time(8, 15)
    # repeat = True
    # active = True

    # save_reminder(
    #     label,
    #     ", ".join(days),
    #     json.dumps(alert_type),
    #     alert_time.strftime("%H:%M:%S"),
    #     repeat,
    # )
    # ------------------------------------------
    #  Update Reminder
    # id = 7
    # label = "Prepare for church"
    # days = ("Sun",)
    # alert_type = {"sound": True, "popup": False}
    # alert_time = time(23, 30)
    # repeat = True
    # active = True

    # update_reminder(
    #     id,
    #     label,
    #     ", ".join(days),
    #     json.dumps(alert_type),
    #     alert_time.strftime("%H:%M:%S"),
    #     repeat,
    #     active,
    # )
    # ------------------------------------------
    ## Delete reminder
    # id = 2
    # delete_reminder(id)
    # ------------------------------------------
    ## Disable/Enable reminder
    # id = 3
    # active = False
    # toogle_state(id, active)
    # ------------------------------------------
    ## List reminder information sorted by time
    # reminders = fetch_all_reminders()
    # print(reminders)
    # ------------------------------------------
    ## Fetch today's reminders
    # reminders = fetch_today_reminders()
    # print(reminders)
    # ------------------------------------------
    ## filter reminder information by `status`, `day` and `state`
    ### status = stage in progress => active
    ### state = current position => Passed/Pending
    # class Reminder:
    # ...:     def fetch_by_day(self):
    # ...:         # call db query function
    # ...:         # build object
    # ...:         return self
    # ...:     def fetch_by_state(self):
    # ...:         # call db query function
    # ...:         # build object
    # ...:         return self
    ########## By day
    # day = "Sun"

    # reminders = fetch_by_day(day)
    # print(reminders)

    ########## By status
    # status = True
    # reminders = fetch_by_active(status)
    # print(reminders)

    ########## By state
    # state = "Pending"
    # reminders = fetch_by_state(state)
    # print(reminders)
    # ------------------------------------------
    ## Search By Label
    # label = "break"
    # reminders = search_by_label(label)
    # print(reminders)
    # ------------------------------------------
    ## Fetch up-coming reminder
    # reminder = fetch_up_coming_reminder()
    # print(reminder)
    # ------------------------------------------
    ## Delete all reminders
    delete_all()
