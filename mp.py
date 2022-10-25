import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
#  #Functional method

# plt.plot(x,y,'r-')
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')
# # plt.show()


# #multiplots
# ##plot1
# plt.subplot(1,2,1)
# plt.plot(x,y,'r')
# ##plot2
# plt.subplot(1,2,2)
# plt.plot(y,x,'b')
# # plt.show()


#Object Oriented Method
fig = plt.figure()
##object gets created
axes = fig.add_axes([0.1,0.1,0.8,0.8])#left,bottom, width, height - all these values should be b\w 0 and 1
axes.plot(x,y)
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Title')
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2, 0.5,0.4, 0.3])
axes1.plot(x,y)
axes2.plot(y,x)
axes1.set_title('Large plot')
axes2.set_title('Small plot')
plt.show()