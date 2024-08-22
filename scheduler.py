import schedule
import time
from datetime import datetime
import pytz

# Your main function that you want to run daily
def run_daily_task():
    print(f"Task started at {datetime.now()}")
    # Call your main ATS function or script here
    # Example: main()

# Function to convert 7:30 AM IST to local time
def convert_ist_to_local(ist_time_str):
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = ist.localize(datetime.strptime(ist_time_str, '%H:%M'))
    local_time = ist_time.astimezone()
    return local_time.strftime('%H:%M')

# Schedule the task daily at 7:30 AM IST
local_time = convert_ist_to_local('07:30')
schedule.every().day.at(local_time).do(run_daily_task)

print(f"Task scheduled to run daily at {local_time} local time.")

while True:
    schedule.run_pending()
    time.sleep(1)
