import os
import datetime


def get_last_modified_date_and_time_of_file_code(file_path):
    modification_time = os.path.getmtime(file_path)
    formatted_modification_time = datetime.datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
    return formatted_modification_time
