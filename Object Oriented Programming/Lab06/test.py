from datetime import datetime, timedelta

current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

date_string = "2022-01-15 12:30:45"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date:", parsed_date)

current_datetime = datetime.now()
future_datetime = current_datetime + timedelta(days=7)
time_difference = future_datetime - current_datetime
print("Time Difference:", time_difference)