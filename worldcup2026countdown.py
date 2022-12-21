import json
import time
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def countdown():
    # Get the current time in unix timestamp
    now = int(time.time())

    # Get the worldcup 2026 date in unix timestamp
    worldcup_2026 = int(datetime(2026, 6, 13).timestamp())

    # Calculate the remaining time in seconds
    remaining_time = worldcup_2026 - now

    # Calculate the remaining time in year, months, days, hours, minutes and seconds
    years, remainder = divmod(remaining_time, 31556926)
    months, remainder = divmod(remainder, 2629743)
    days, remainder = divmod(remainder, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Create a json with the remaining time
    data = {'year': years, 'months': months, 'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds, 'unix_time': remaining_time, 'app_ver': '1.0'}

    return json.dumps(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18080)
