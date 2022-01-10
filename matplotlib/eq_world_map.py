import plotly.express as px
import eq_explore_data as eq
import pandas as pd

"""
magl = map(abs, eq.mags)
print(magl[:10])

magl = []
for mag_l in eq.mags:
    mag = mag_l + 1
    magl.append(mag)
print(magl[:10])
"""

data = pd.DataFrame(data=zip(eq.lons, eq.lats, eq.titles, eq.mags), columns=["经度", "纬度", "位置", "震级"])
data.head()

fig = px.scatter(
    data,
    x="经度",
    y="纬度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
    size="震级",
    size_max=11,
    color="震级",
)

fig.write_html("data/global_earthquakes.html")
fig.show()
