import time
from datetime import datetime

time_now = time.time()
time_format = datetime.utcfromtimestamp(time_now).strftime('%b %d %Y')
time_seconds = "{:,.4f}".format(time_now)
time_sci = "{:.2e}".format(time_now)

print(f"Seconds since January 1, 1970: {time_seconds}\
       or {time_sci} in scientific notation")
print(time_format)
