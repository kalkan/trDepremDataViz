import geopandas
import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 10), dpi=100)

eq = geopandas.read_file("./Data/tr-40years-depremdata.shp")
tr = geopandas.read_file("./Data/gadm36_TUR_0.shp")

#mag str to numeric 
eq['mag_num'] = pd.to_numeric(eq['mag'])

#eq.head()
#tr.plot()
#eq.plot()


base = tr.plot(ax=ax, color='white', edgecolor='black')
eq.plot(ax=base, marker='o', color='red', edgecolor='b', alpha=0.5, markersize=eq['mag_num'])

ax.set(title='>4 Magnitude Depremler (1970-2020)')
#ax.legend(fontsize=20,
#          frameon=True,
#          loc=(1, .1),
#          title="LEGEND")
plt.show()

