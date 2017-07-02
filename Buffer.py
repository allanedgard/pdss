class Buffer(object):

	def __init__(self):
		self.dict = dict()
		self._lastTime = 0

	def add (self, timestamp, Message):
		if timestamp not in self.dict:
			self.dict[timestamp] = []
		self.dict[timestamp].append(Message)
		return

	def list(self, timestamp):
		x =  self.dict[timestamp]
		del(self.dict[timestamp])
		return x

	def checkTime(self, timestamp):
		if timestamp in self.dict:
			return True
		else:
			return False

	def getMsgs(self, timestamp):
		x = []
		for i in range(self._lastTime, timestamp + 1):
			if self.checkTime(i):
				y = self.list(i)
				for z in y:
					x = x + [ (i, z) ]
		self._lastTime = timestamp
		return x
