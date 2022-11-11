import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
print(tips.head())

#DIDTRIBUTION PLOT kde - kernel density estimation
# sns.distplot(tips['total_bill'], kde=False, bins=30) - give warning
# sns.displot(tips['total_bill'], kde=False, bins=40)

#jointplot
# sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex') #kind=hex, defalut=scattered
# # fig.savefig('my_seaborn.jpg')


#pairplot
# sns.pairplot(tips, hue='sex',palette='coolwarm')
# # fig.savefig('pairplot_hue.jpg')

#RUG PLOT
# sns.rugplot(tips)
# sns.rugplot(tips['total_bill'])


# plt.show()
# sns.kdeplot(tips['total_bill'])
# plt.show()




#CATEGORICAL PLOTS

