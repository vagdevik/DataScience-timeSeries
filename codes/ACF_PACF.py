import numpy as np
import pandas as pd
from pandas import Series
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf

#read from csv
series = Series.from_csv('_sunglasses.csv',header=0)
series.plot()
pyplot.title("Data Plot")
pyplot.show()
data = pd.read_csv("_sunglasses.csv")

#extract data values
zt = np.array(data.Sales)

#mean of data
mean = np.mean(zt)

#variance of data
#var = zt.var()
c0 = np.sum((zt - mean)*(zt - mean))/len(zt)

#calculate lag-wise auto-correlation
corr_coeffs=[]
lags=[]

for k in range(len(zt)):
	series_1 = zt[k:]
	series_2 = zt[:len(zt)-k]
	
	if len(series_1)!=len(series_2):
		print "Error!!!"
	else:
		num = np.sum((series_1 - mean)*(series_2 - mean))
		den = c0*len(zt)
		coeff = num/den
	
		corr_coeffs.append(coeff)
		lags.append(k)

print "************************"
print "correlation coeffs: ",corr_coeffs
print "------------"
print "lags: ",lags
print "************************"

#plot autocorr vs lag
pyplot.title("calculated")
pyplot.bar(lags,corr_coeffs,width=0.2)
pyplot.axhline(0)
pyplot.show()

#plot the same using in-built func
plot_acf(zt)
pyplot.show()
	
