from datetime import datetime
date1 = datetime(2024, 2, 10, 12, 0 , 0)
date2 = datetime(2024, 2, 13, 14, 30, 0 )
difference = date2 - date1
difference.total_seconds()
print(f"Difference in seconds: {difference}")
