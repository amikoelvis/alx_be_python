from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_time, days_to_add):
    future_date = current_time + timedelta(days=days_to_add)
    print("Future date: ", future_date.strftime("%Y-%m-%d"))
    return future_date

if __name__ == "__main__":
    current = display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current, days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")
