from socket import *
import threading
import time

class SocketClient(threading.Thread):

	def __init__(self, ip, port):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port

	def run(self):
		s = socket(AF_INET, SOCK_DGRAM)
		s.bind( (self.ip, self.port) )
		while True:
			data, addr = s.recvfrom(512)
			print addr, data
			time.sleep(0.00001)

class Agent:

	def __init__(self, ip, port):
		self.port = port
		self.ip = ip
		newThread = SocketClient(ip, port)
		newThread.start()
		newThread.join()

	def connectTo(self,toPort):
		self.toPort = toPort

	def send(self,msg):
		s = socket(AF_INET, SOCK_DGRAM)
		s.sendto(msg, (self.ip, self.toPort) )
		time.sleep(0.00001)
