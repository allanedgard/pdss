import Randomize
import rpy2.robjects as robjects
import matplotlib.pyplot as plt


x=Randomize.Randomize(0)
y=Randomize.Randomize(0)
robjects.r('set.seed(42)')
for i in range(10):
	print x.R('rnorm(1000000,20,5)')
'''
print x.expntl(12.0)
print x.erlang(2.0, 1.0)
print x.normal(2.0, 0.5)
print y.handle('normal(2.0, 0.5)')
print x.normal(2.0, 0.5)
print x.normal(2.0, 0.5)
print x.normal(2.0, 0.5)
print x.normal(2.0, 0.5)
print y.normal(2.0, 0.5)
print y.normal(2.0, 0.5)
print y.normal(2.0, 0.5)
print y.normal(2.0, 0.5)
plt.hist(x.geraLN(1000000),100)
plt.show()
plt.hist(x.geraE(1000000),100)
plt.show()
plt.hist(x.geraN(1000000),100)
plt.show()
plt.hist(x.geraER(1000000),100)
plt.show()
plt.hist(x.geraU(1000000),100)
plt.show()
plt.hist(x.geraH(1000000),100)
plt.show()
print x.irandom(20,30)
'''
