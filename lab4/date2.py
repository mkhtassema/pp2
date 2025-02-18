from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
print(f"Yesterday: {yesterday}")
print(f"today: {today}")
print(f"tomorrow: {tomorrow}")