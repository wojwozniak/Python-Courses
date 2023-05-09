# FCC Course: Scientific Computing with Python
# Project: Time Calculator
# Author: Wojciech Woźniak
# Date: 10.05.2023



# Date object import
from datetime import datetime


# Main function
def add_time(start, duration, *day):
    
    # Convert time to 24 hour format
    time_1 = datetime.strptime(start, "%I:%M %p")
    
    # Split duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    # Calculate total minutes
    total_minutes = (
        time_1.hour * 60 + time_1.minute + 
        duration_hours * 60 + duration_minutes
    )
    
    # Calculate output hours and minutes
    output_hours = total_minutes // 60
    output_minutes = total_minutes % 60
    
    # Calculate days delta
    days_delta = output_hours // 24
    
    # Fix output hours after calculating days delta
    output_hours = output_hours % 24
    
    # AM or PM
    if output_hours < 12:
        period = 'AM'
    else:
        period = 'PM'
        output_hours -= 12
    
    # Fix 0 AM and 0 PM
    if output_hours == 0:
        output_hours = 12
    
    
    # Format the output string with leading zeros for minutes
    output_str = "{}:{:02d} {}".format(output_hours, output_minutes, period)

    # Add day of the week if provided
    if day:
        day_str = day[0].capitalize()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = (days.index(day_str) + days_delta) % 7
        output_str += ", {}".format(days[day_index])

    # Add delta to the output string
    if days_delta == 0:
        delta_str = ""
    elif days_delta == 1:
        delta_str = " (next day)"
    else:
        delta_str = " ({} days later)".format(days_delta)
    output_str += delta_str
    
        
    return output_str