import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
 #Functional method

plt.plot(x,y,'r-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()


#multiplots
##plot1
plt.subplot(1,2,1)
plt.plot(x,y,'r')
##plot2
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()