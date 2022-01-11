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

fig = px.scatter_mapbox(
    data,
    lon="经度",
    lat="纬度",
    # range_x=[-200, 200],
    # range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
    size="震级",
    size_max=11,
    color="震级",
    hover_name="位置",
    zoom=0,
    center={"lat": 37, "lon": 101}
)
fig.update_layout(mapbox={'accesstoken': 'pk.eyJ1IjoidGh6aHViIiwiYSI6ImNreTlleDh1ZjA1cTgydm55cTE5ZHc4N2QifQ.sW3YhTZLDUEzq0t8ZgziHg', 'style': 'basic'},
                  title=dict(x=0.5, xref='paper'),
                  margin={'l': 10, "r": 100, 't': 10, 'b': 0}
                  )

fig.write_html("data/global_earthquakes.html")
fig.show()
