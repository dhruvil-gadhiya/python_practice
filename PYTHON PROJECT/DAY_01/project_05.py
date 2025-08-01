# Project Title: Simple Alarm Clock...
# Question: Create a Python program where the user can input a time (e.g., 07:30), and the program will notify them when that time arrives. Use the system clock and a sound or print message as the alarm...

import datetime
import time

alarm_time = input("Enter alarm time in HH:MM format (24-hour clock): ")

try:
    alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
    
    print(f"Alarm is set for {alarm_hour:02d}:{alarm_minute:02d}...\nWaiting for the alarm time...")

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("\n⏰⏰⏰ ALARM! It's time! ⏰⏰⏰")
            break

        time.sleep(30)

except ValueError:
    print("Invalid time format. Please enter time as HH:MM (e.g., 07:30).")
