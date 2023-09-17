# Step one, checking if code is existant and downloaded if not
import urllib.request
import os
from collections import Counter

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
filename = 'log.txt'

# Check if the file already exists
if os.path.exists(filename):
    print(f"The file '{filename}' already exists.")
else:
    print(f"Downloading '{filename}'...")
    urllib.request.urlretrieve(url, filename)
    print(f"'{filename}' has been downloaded.")

# rest of the code will go after this

from datetime import datetime

# define log file path

log_file_path = 'log.txt'

# initialize list to store log entries
log_data = []

# read log entries from the log.txt file

try:
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()
except FileNotFoundError:
    print(f"The file '{log_file_path}' does not exist or cannot be accessed.")
    
print("--------------------------------------------------")

# time period from last 6 months
start_date = datetime(1995, 4, 11)  # April 11, 1995
end_date = datetime(1995, 10, 12)   # October 11, 1995

total_requests_in_6_months = 0  # Initialize the variable to hold the count

for log_entry in log_data:
    if "[" in log_entry:
        date_str = log_entry.split("[")[1].split(" ")[0]
    log_date = datetime.strptime(date_str, "%d/%b/%Y:%H:%M:%S")

    if start_date <= log_date <= end_date:
        total_requests_in_6_months += 1  # Increment the count if it falls within the period

# Decrement the count after the loop
total_requests_in_6_months -= 1

# Now 'total_requests_in_6_months' contains the total requests made in the 6 months
print(f"Total requests made in the last 6 months: {total_requests_in_6_months}")

print("--------------------------------------------------")

# total time period 
start_date2 = datetime(1994, 10, 24)  # October 24, 1994
end_date2 = datetime(1995, 10, 12)   # October 11, 1995

total_requests2 = 0  # Initialize the variable to hold the count

for log_entry in log_data:
   
    if start_date2 <= log_date <= end_date2:
        total_requests2 += 1  # Increment the count if it falls within the period

print(f"Total requests made in the time period: {total_requests2}")

print("--------------------------------------------------")

#------steps 5 and 6 code
#initialize list for files
file_list = []
#iterate through each log entry to make list of files
for log in log_data:
    full_line = []
    line = []
    full_line = log.split("GET ") #split line into lest where second element begins w file name
    if len(full_line) > 1: # check if line is valid request
        line = full_line[1].split(" ") #split elemnet containing file to isolate name
        file = line[0] #define file var
        file_list.append(file) #add file to list
    else: # if is default to index, don't count as request
        continue

file_counts = Counter(file_list) #use Counter to count occurences of each file

most_freq = file_counts.most_common(1) #set most recurring file
least_freq = file_counts.most_common()[:-2:-1] # set least reccuring file

#print output
print(f"Most requested file: {most_freq[0][0]} (Count: {most_freq[0][1]})")
print("--------------------------------------------------")
print(f"Least requested file: {least_freq[0][0]} (Count: {least_freq[0][1]})")
print("--------------------------------------------------")

    

