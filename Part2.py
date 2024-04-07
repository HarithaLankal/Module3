def calculate_alarm_time(current_time, hours_to_wait):
    total_hours = current_time + hours_to_wait
	# Time wraps at 24 hours. Adding modulo division for that
    alarm_time = total_hours % 24  
    return alarm_time

def main():
    try:
        current_time = int(input("Enter the current time (in hours, 0-23): "))
        hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

        if current_time < 0 or current_time >= 24 or hours_to_wait < 0:
            raise ValueError("Please enter a valid time ( 0 to 23) and number of hours (>0).")

        alarm_time = calculate_alarm_time(current_time, hours_to_wait)
        print(f"The alarm will go off at {alarm_time}:00")
		
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()