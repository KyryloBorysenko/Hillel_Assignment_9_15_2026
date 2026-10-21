seconds = int(input("How much seconds: "))

# Takes value from seconds and then divide it
days, seconds = divmod(seconds, 86400) # divide seconds and seconds(day) then days takes the first value and seconds variable change value to the reminder
hours, seconds = divmod(seconds, 3600) # divide seconds and seconds(hours) then days takes the first value and seconds variable change value to the reminder
minutes, seconds = divmod(seconds, 60) # divide seconds and seconds(minutes) then days takes the first value and seconds variable change value to the reminder

if days == 1:
    dayWord = "day"
else:
    dayWord = "days"

# Adds zeros if needed
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

# Print our days, hours, minutes, and seconds
print(f"{days} {dayWord} {hours}:{minutes}:{seconds}")