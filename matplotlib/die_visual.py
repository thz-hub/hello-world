from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

print(results)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

x_value = list(range(1, die.num_sides + 1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷色子', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
