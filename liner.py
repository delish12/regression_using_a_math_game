import numpy as np
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel('stats.xlsx')

names = list(set(df['name']))
names.sort()
for idx,val in enumerate(names):
    print(idx+1,val)
choices = list(map(int,input('enter the numbers wanted=').split()))
choices = list(map(lambda a : a-1,choices))

def dynamic_plotting(name,noc,i):
    rows = df.loc[df['name']==name]

    dy = rows['avg_score'].to_numpy()

    dx = np.arange(len(dy))

    slope, intercept, r, p, std_err = stats.linregress(dx,dy)

    def myfunc(x):
        return slope*x + intercept

    mymodel = list(map(myfunc,dx))

    
    plt.subplot(noc,1,i+1)
    plt.xlabel('time_stamp')
    plt.ylabel('avg_score')
    plt.ylim(ymax = 1)
    plt.scatter(dx,dy)
    plt.title(name)
    plt.plot(dx,mymodel)

noc = len(choices)
for idx,val in enumerate(choices):
    dynamic_plotting(names[val],noc,idx)

plt.show()
