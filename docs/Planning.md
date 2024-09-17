# Remind Me App

This is a refined version of the [remindme-app](https://github.com/Eyongkevin/remindme-app).

Here are some major non-functional changes from the old version
- It's more portable since it now uses sqlite3 and not postgresql
- It's more flexible as it uses `kivyMD` and  will be tested on these systems: `windows`, `Mac`, `Linux`.
- Contains more test coverage with a CI-CD pipeline
- Deployed on `pypi`.


## Screens
Here are the screens that will be developed

- Home
- ListRemainder
    - ReminderConfig
- TimeTracker
    - TimeTrackerConfig

## Tech Stack
After the old version, here are some important tech stacks
- Python
- Kivy
- KivyMD
- Sqlite3
- pytest
- schedule
- aiosql

## Screen Details
For version 1, screens will contain the following

### Home
This will be the default page when you start the application. It will contain the following.

- The upcoming remainder event
    - label
    - time and date
    - remaining time before event that decrement in real-time
- A graphical representation of the current day's remainders that shows a line graph indicating the remainders and the time distance between them.

### ListRemainder
This screen should list all remainders (sorted by time/day) that have been set in the application.

This screen should have
- Remainder items in a scroll-down list
- `Add+` button to add remainder events
- Search bar to search remainder by label
- Filters to filter by 
    - remainder status
    - yesterday, today, tomorrow, date and date range, all.
    - active state
        - active state should be default filter
- A button to show a calendar showing all remainders.


Each reminder item should have the following:

- label
- time
- date
- is_active
- status[`pending`, `passed`]
- note
- action buttons
    - delete
    - toggle activation
        - Count number of the specific days(default to 1)
        - Always
    - edit

### ReminderConfig
This should be a `popup` to the **ListRemainder** screen. It contains configurations to add/update remainder events

- Time
- Days
    - Once
    - Repeat
        - Every `2nd` Fridays for example, default to `1`.
- Date
    - Once
    - Repeat
        - month-day(dd/mm): Repeat every `dd/mm` of each year.
        - day(dd): Repeat every `dd` of each month
- Alarm type
    - Popup notification
    - play Sound 
        - Select sound from computer(app sound is default)
        - Sound will be path to sound from the computer.
- Alarm delay
    - Default to 5 minutes before time, but should be configurable.
- Label
- Note
- Buttons
    - Reset
    - Add
- Cron job notification for a successfully added remainder. 


# TimeTracker
This screen will contain functionalities that has to do with tracking time. It will display the time, timezone and date in real-time base on the system's timezone

This screen will contain the following main tabs
- Stop watch
    - Buttons: `start`, `pause`, `reset`
        - The `start` helps us set the timer, with the option to have a count down or count up. We **shouldn't** be able to update the time once set.
        - The `pause` will pause the timer
        - The `reset` will stop and reset the timer.
    - real-time timer 
- Pomodoro tracker
    - Create event to be tracked. Each event will have
        - label
        - note
        - work/rest time
        - sound/popup when work/rest times are reached.
            - sound when work time starts
            - sound when rest time starts
        - is_active that indicates if the specific event is active
        - start_at: To program when it should start
        - ends_at: To program when it should stop
        - Days: Days it should run once or repeatedly
        - Repeat: If it should repeat for those days or not.
        - belong_to_reminder: If it belongs to a remainder or not. and if it does, then it will be managed by that remainder. For example, it stops when the remainder has passed.
        - alarm_delay: How many minutes to the start times
    
