import random
import math
import rpy2.robjects as robjects

# That class implements probabilistic distribution functions from SMPL
# and allows for integration to all functions available from R environment
# tracing and reflection support (to be used in PDSS) are still missing

class Randomize:

	def __init__(self,seed1=None):
		random.seed(seed1)
		self.__z2 = 0.0
		self.__x = None
		self.__function = None
		self.__next = 0

	def expntl (self,x):
		return -x * math.log(random.random())

	def erlang (self, x, s):
		if s>x:
			raise Exception('s > x in Erlang')
		z=x/s
		k = int(z * z)
		z = 1.0
		for i in range(0, int(k-1)):
			z = z * random.random()
		return -(x/k) * math.log(z)

	def uniform(self, a=0.0, b=1.0):
		return a+(b-a)*random.random()

	def irandom(self, i, n):
		n = n-i
		n = int((n+1.0)*random.random())
		return i+n

	def hyperx(self, x, s):
		if (s<=x):
			raise Exception('s <= x in hyperx')
		cv = s /x
		z = cv*cv
		p = 0.5*(1.0- math.sqrt((z-1.0)/(z+1.0)) )
		if random.random() > p:
			z = x/(1.0-p)
		else:
			z = x/p
		return -.5*z*math.log(random.random())

	def normal(self, x, s):
		if  (self.__z2 != 0.0):
			z1 = self.__z2
			self.__z2 = 0.0
		else:
			v1 = 2 * random.random() - 1.0
			v2 = 2 * random.random() - 1.0
			w  = v1*v1+v2*v2
			while (w>=1.0):
				v1 = 2 * random.random() - 1.0
				v2 = 2 * random.random() - 1.0
				w  = v1*v1+v2*v2
			w = math.sqrt((-2.0*math.log(w))/w)
			z1 = v1*w
			z2 = v2*w
		return x+z1*s

	def lognormal(self, x, s):
		xn = math.log(x)-0.5*math.log(1+(s*s/(x*x)))
		sn = math.log((s*s/(x*x))+1)
		return math.exp(self.normal(xn, sn))

	def R(self, function):
		if self.__x == None:
			self.__x = self.R1(function)
		if self.__function != function:
			self.__next = 0
		self.__function = function
		n = self.__x[self.__next]
		self.__next = ( self.__next + 1 ) % len(self.__x)
		return n

	def R1(self, function):
		self.__x = robjects.r(function)
		return self.__x

	def setDistribution(self, dist):
		pass

	def genericDistribution(self):
		pass

	def tracing(filename, column):
		pass

	def handle(self,action):
  		if hasattr(self,action):
    			method = getattr(self,action)
    			method()
  		else:
    			print 'Metodo inexistente'

	def geraN(self, n):
		return [self.normal(2.0,0.5) for i in range(n)]

	def geraE(self, n):
		return [self.expntl(1.5) for i in range(n)]

	def geraER(self, n):
		return [self.erlang(4.0,2.0) for i in range(n)]

	def geraLN(self, n):
		return [self.lognormal(2.0,1.0) for i in range(n)]

	def geraU(self, n):
		return [self.uniform(0.0,10.0) for i in range(n)]

	def geraH(self, n):
		return [self.hyperx(2.0,3.0) for i in range(n)]
