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


# fig = plt.figure()

# ##object gets created

# axes = fig.add_axes([0.1,0.1,0.8,0.8])#left,bottom, width, height - all these values should be b\w 0 and 1
# axes.plot(x,y)
# axes.set_xlabel('X label')
# axes.set_ylabel('Y label')
# axes.set_title('Title')



# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2, 0.5,0.4, 0.3])
# axes1.plot(x,y)
# axes2.plot(y,x)
# axes1.set_title('Large plot')
# axes2.set_title('Small plot')
# plt.show()

###Subplot
# fig,axes = plt.subplots(nrows=3,ncols=3)
# plt.tight_layout() - overlappng avoid
# axes.plot(x,y)

fig,axes = plt.subplots(nrows=1,ncols=2)

#*******iterate*********

# for current_ax in axes:
#     current_ax.plot(x,y)

#******index************

# axes[0].plot(x,y)
# axes[0].set_title('First')
# axes[1].plot(y,x)
# axes[1].set_title('Second')

# plt.show()


#Figure size, Aspect ratio and DPI

# fig = plt.figure(figsize=(8,2))#dots per inch
# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y)


# fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))#dots per inch
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.tight_layout()
# plt.show()


#SAVE FIGURE

fig.savefig('my_picture.jpg',dpi=200)


