import time
from datetime import datetime, timedelta

# Calculate the date and time of the next World Cup
world_cup_date = datetime(2026, 6, 13)

# Display the countdown
while True:
    # Calculate the current date and time
    current_time = datetime.now()
    
    # Calculate the time remaining until the World Cup
    time_remaining = world_cup_date - current_time
    
    # Split the time remaining into years, months, days, etc.
    years, remainder = divmod(time_remaining.days, 365)
    months, days = divmod(remainder, 30)
    hours, minutes = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(minutes, 60)
    
    # Display the countdown
    print(f"Time remaining until the next World Cup: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    
    # Wait 1 second before updating the countdown
    time.sleep(1)
