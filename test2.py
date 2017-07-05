import Agent
x = Agent.Agent('127.0.0.1', 12345)
y = Agent.Agent('127.0.0.1', 54321)
x.connectTo(y.port)
y.connectTo(x.port)
x.send('de x para y')
y.send('de y para x')
