import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('stats.xlsx')
names = list(set(df['name']))
names.sort()

def poly_reg(name,noc,i,num):
        
    rows = df.loc[df['name']==name]

    y = rows['avg_score']

    x = np.arange(len(y))

    mymodel = np.poly1d(np.polyfit(x,y,num))

    lines = np.linspace(0,x[-1],len(x)*30)


    plt.subplot(noc,1,i)
    plt.scatter(x,y)
    plt.ylabel('avg_score')
    plt.title(name)
    plt.ylim(ymax = 1,ymin = 0)
    plt.plot(lines,mymodel(lines))


for idx,val in enumerate(names):
    print(idx+1,val)

choices = list(map(int,input('enter the no.of choices=').split()))
num = int(input('what order ='))
noc = len(choices)
for idx,val in enumerate(choices):
    poly_reg(names[val-1],noc,idx+1,num)

plt.show()

