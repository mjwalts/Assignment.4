# use same downloading process in assignment 3
import urllib.request
import os

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
filename = 'log.txt'

# Check if the file already exists
if os.path.exists(filename):
    print(f"The file '{filename}' already exists. Starting analysis:")
else:
    print(f"Downloading '{filename}'...")
    urllib.request.urlretrieve(url, filename)
    print(f"'{filename}' has been downloaded. Starting analysis:")
    
print("----------------------------------------------------")

from datetime import datetime, timedelta

# Define log file path
log_file_path = 'log.txt'

# store requests per week and per month
day_requests = {}
week_requests = {}
month_requests = {}

# read log entries
try:
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()
except FileNotFoundError:
    print(f"The file '{log_file_path}' does not exist or cannot be accessed.")

# process log entries
for log_entry in log_data:
    if "[" in log_entry:
        date_str = log_entry.split("[")[1].split(" ")[0]
        log_date = datetime.strptime(date_str, "%d/%b/%Y:%H:%M:%S")
        day_str = log_date.strftime("%B %d, %Y")  # format date to MM-DD-YYY
        
        # requests per day count
        if day_str in day_requests:
            day_requests[day_str] += 1
        else:
            day_requests[day_str] = 1
        
        # requests per week count
        while log_date.weekday() != 6:  # finds first Sunday before October 24th
            log_date -= timedelta(days=1)
        
        # determine the start and end dates for the week
        start_date = log_date
        end_date = start_date + timedelta(days=6)
        
        # start week day (Sunday)
        week_range = start_date.strftime("%B %d, %Y")
        
        if week_range in week_requests:
            week_requests[week_range] += 1
        else:
            week_requests[week_range] = 1
        
        # separate month calculation
        month_date = datetime.strptime(date_str, "%d/%b/%Y:%H:%M:%S")

        # requests per month count
        month_year = month_date.strftime("%B of %Y")  
        if month_year in month_requests:
            month_requests[month_year] += 1
        else:
            month_requests[month_year] = 1

# requests per day
for day, count in day_requests.items():
    print(f"{count} Requests made on {day}.")

print("--------------------------------------------------")

# print requests made per week
for week, count in week_requests.items():
    print(f"{count} Requests Made for the Week of {week}.")

print("--------------------------------------------------")

# print requests made per month
for month, count in month_requests.items():
    print(f"{count} Requests Made in {month}.")