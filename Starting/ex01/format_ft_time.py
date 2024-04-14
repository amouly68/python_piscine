import datetime


timestamp = datetime.datetime.now().timestamp()
formatted_timestamp = "{:,.4f}".format(timestamp)
current_date = datetime.datetime.now().strftime("%b %d %Y")


print("Seconds since January 1, 1970:", formatted_timestamp, "or {:.2e} in scientific notation".format(timestamp))
print(current_date)
