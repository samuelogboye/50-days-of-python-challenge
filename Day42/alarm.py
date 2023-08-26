#!/usr/bin/python3


import winsound
import time

def alarm():
    # Get alarm time from the user
    alarm_hour = int(input("Enter the hour for the alarm: "))
    alarm_minute = int(input("Enter the minute for the alarm: "))

    # Get the current time
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min

    # Calculate the time difference for the alarm
    if alarm_hour < current_hour or (alarm_hour == current_hour and alarm_minute <= current_minute):
        alarm_hour += 24  # Alarm is set for the next day

    time_difference = (alarm_hour - current_hour) * 3600 + (alarm_minute - current_minute) * 60

    # Print the alarm time
    print(f"Alarm is set for {alarm_hour:02d}:{alarm_minute:02d}")

    # Wait for the alarm time
    time.sleep(time_difference)

    # Play the alarm sound using winsound
    frequency = 1000  # Adjust the frequency as desired
    duration = 2000  # Adjust the duration as desired
    winsound.Beep(frequency, duration)

# Call the alarm function
alarm()
