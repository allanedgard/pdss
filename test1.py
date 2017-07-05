import Buffer
import time
y = int(time.time()*1000)
time.sleep(.001)
x = Buffer.Buffer()
x.add(int(time.time()*1000)%y, 'teste 1')
x.add(int(time.time()*1000)%y, 'teste 2')
time.sleep(.001)
x.add(int(time.time()*1000)%y, 'prova 3')
x.add(int(time.time()*1000)%y, 'prova 4')
print x.getMsgs(int(time.time()*1000)%y)
time.sleep(.001)
x.add(int(time.time()*1000)%y, 'teste 1')
x.add(int(time.time()*1000)%y, 'teste 2')
time.sleep(.001)
x.add(int(time.time()*1000)%y, 'prova 3')
print x.getMsgs(int(time.time()*1000)%y)

