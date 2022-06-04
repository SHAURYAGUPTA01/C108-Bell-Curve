import random

#print(dice1,dice2)
count=[]
dice_result = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

import plotly.express as px

# fig = px.bar( x=dice_result , y=count)
# fig.show()

import plotly.figure_factory as ff

# draws a distribution plot
fig = ff.create_distplot( [dice_result] , ["sum of dice number"] , show_hist = False )

fig.show()