# 15-6 Two D8s
    # Create a simulation show what happens when you roll two D8 dice 1000 times
    # Predict what the graph would look like and test to see if you were correct
    # Then increase the amount of rolls until your system starts to have issues (10_000_000)

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die(8)
die_1_min = 1
die_2 = Die(8)
die_2_min = 1

max_result = die_1.num_sides + die_2.num_sides
min_result = die_1_min + die_2_min

results = []
frequencies = []

for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

for value in range(min_result, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_vaules = list(range(min_result, max_result+1))
data = [Bar(x=x_vaules, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d8_d8.html')
offline.plot({'data':data, 'layout':my_layout}, filename='d8_d8.html')