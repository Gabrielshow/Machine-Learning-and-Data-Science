# visualization of data using matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from  scipy import stats

s = pd.Series([14,42,65,76,53,3])
y = pd.Series([100,191,222,444,501,46])

slope, intercept, r, p, std_err = stats.linregress(s, y)
def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, s))

plt.plot(s, mymodel)
plt.show()

# Bar plot
# df = df.groupby('month')[['cases', 'deaths']].sum()
# df.plot(kind = "bar", stacked = True)
# kind = "barh" can be used to create a horizontal bar chart
# kind = "box", box shows upper & lower quartiles
# green lines represents median value
