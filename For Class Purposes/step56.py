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

#------steps 5 and 6 code
#initialize list for files
file_list = []
#iterate through each log entry
for log in log_data:
    full_line = []
    line = []
    full_line = log.split("GET ") #split line into lest where second element begins w file name
    if len(full_line) > 1: # check if issa weird line
        line = full_line[1].split(" ") #split elemnet containing file to isolate name
        file = line[0] #define file var
        file_list.append(file) #add file to list
    else:
        continue

file_counts = Counter(file_list) #use Counter to count occurences of each file

most_freq = file_counts.most_common(1) #set most recurring file
least_freq = file_counts.most_common()[:-2:-1] # set least reccuring file

#print output
print(f"Most requested file: {most_freq[0][0]} (Count: {most_freq[0][1]})")
print(f"Least requested file: {least_freq[0][0]} (Count: {least_freq[0][1]})")

    


    

