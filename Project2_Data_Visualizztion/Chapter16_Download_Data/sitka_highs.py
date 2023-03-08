import csv
import matplotlib.pyplot as plt

filename = 'Chapter16_Download_Data/data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get high temps from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)


# Plot the high temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot
ax.set_title('Daily high temperatures, July 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()