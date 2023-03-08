# 16-1 Sitka Rainfall
    # Use the dataset sitka_weather_1028_simple.csv
    # Use the PRCP which represents daily rainfall amounts.
    # Make a visualization focusing on the data in this column

import csv
import matplotlib.pyplot as plt
from datetime import datetime

dataset = 'Chapter16_Download_Data/TIY/tiy_data/sitka_weather_2018_simple.csv'

with open(dataset) as ds_file:
    reader = csv.reader(ds_file)
    header_row = next(reader)

    dates, rain = [], []
    
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        PRCP = float(row[3])
        dates.append(current_date)
        rain.append(PRCP)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rain, c='blue')

ax.set_title('Daily rain amount - 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rain in Inches', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()