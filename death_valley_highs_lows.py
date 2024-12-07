from pathlib import  Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path=Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

lows,dates,hights = [],[],[]

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        hights.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots(figsize=(10, 6), dpi=80)
ax.plot(dates,hights,color='red',alpha=0.5) # 0表示完全头面，1 表示完全不透明
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,hights,lows,facecolor='blue',alpha=0.1)
ax.set_title("daily high and low temperatures, 2021\nDeath Valley,CA",fontsize =20)
ax.set_xlabel('',fontsize = 14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)",fontsize = 14)
ax.tick_params(labelsize=16)
plt.show()
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

