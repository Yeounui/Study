import matplotlib.pyplot as plt
import numpy as np


xdata = np.arange(1, 120, 0.2)

# create some y data points
ydata1 = [np.math.factorial(i) for i in np.floor(xdata)]
ydata2 = np.log(xdata)
ydata3 = xdata
ydata4 = np.full(xdata.size, 1)
ydata5 = 2 ** xdata
ydata6 = xdata ** np.log(xdata)
ydata7 = xdata ** 2
ydata8 = xdata ** xdata

# plot the data
plot1 = plt.plot(xdata, ydata1, label= "n!", color='#38E063')
plot2 = plt.plot(xdata, ydata2, label= "log n", color='#3240E0')
plot3 = plt.plot(xdata, ydata3, label= "n", color='#AEE02D')
plot4 = plt.plot(xdata, ydata4, label= "1", color='#E01623')
plot5 = plt.plot(xdata, ydata5, label= "2**n", color='#E0BB31')
plot6 = plt.plot(xdata, ydata6, label= "n*log n", color='#E07B2E')
plot7 = plt.plot(xdata, ydata7, label= "n**2", color='#922DE0')
plot8 = plt.plot(xdata, ydata8, label= "n**n", color='#3BC7E0')

plt.legend(loc='upper right')

# set the limits
plt.xlim([1, 120])
plt.ylim([0, 1000])

plt.xlabel('n')
plt.ylabel('f(n)')

plt.title('Complexity')

# display the plot
plt.show()