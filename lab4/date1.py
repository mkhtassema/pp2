from datetime import date, timedelta
today = date.today()
five_days_ago = today - timedelta(days = 5)
print(f"today: {today}")
print(f"five days ago: {five_days_ago}")


