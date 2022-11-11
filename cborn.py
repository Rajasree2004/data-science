import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')
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
# sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
# plt.show()

# sns.countplot(x='sex', data=tips)#eztimator count no. of occurences
# plt.show()

# sns.boxplot(x='day',y='total_bill',data=tips)
# #hue gives different level of data
# sns.boxplot(x='day',y='total_bill',data=tips, hue='smoker')
# plt.show()

# sns.violinplot(x='day', y='total_bill',data=tips)

# sns.violinplot(x='day', y='total_bill',data=tips, hue='sex')
# plt.show()

# sns.stripplot(x='day', y='total_bill',data=tips)
# plt.show()
# sns.stripplot(x='day', y='total_bill',data=tips, jitter=True)
# plt.show()

# sns.swarmplot(x='day', y='total_bill', data=tips)#strip+violin
# plt.show()

# sns.factorplot(x='day',  y='total_bill' , data=tips , kind='bar')#kind arg describes factor plot
# plt.show()


#MATRIX PLOTS
flights.head()
tc = tips.corr()
# sns.heatmap(tc)
# sns.heatmap(tc, annot=True, cmap='coolwarm')
# plt.show()


#data in matrix from
fp = flights.pivot_table(index='month', columns='year', values='passengers')
# # sns.heatmap(fp)
# sns.heatmap(fp, cmap='magma', linecolor='white', linewidth=1)
# plt.show()  

# sns.clustermap(fp)

# sns.clustermap(fp, cmap='coolwarm', standard_scale=1)
# plt.show()


#GRID
iris.head()

