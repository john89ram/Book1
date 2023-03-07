# 15-7 Three D6s
    # Create a vis that shows what happens with you roll 3 D6 dice

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_1_min = 1
die_2 = Die()
die_2_min = 1
die_3 = Die()
die_3_min = 1

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
min_result = die_1_min + die_2_min + die_3_min

results = []
frequencies = []

for roll in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
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
offline.plot({'data':data, 'layout':my_layout}, filename='3_D8s.html')