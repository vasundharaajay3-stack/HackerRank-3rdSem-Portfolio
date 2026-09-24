s = input().strip()

hour = int(s[0:2])
ampm = s[-2:]

if ampm == "AM":
    if hour == 12:
        hour = 0
else:
    if hour != 12:
        hour += 12

print(f"{hour:02d}" + s[2:-2])
