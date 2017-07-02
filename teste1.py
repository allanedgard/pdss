import Buffer

x = Buffer.Buffer()
x.add(10, 'teste 1')
x.add(10, 'teste 2')
x.add(12, 'prova 3')
x.add(14, 'prova 4')
print x.getMsgs(14)
x.add(16, 'teste 1')
x.add(17, 'teste 2')
x.add(18, 'prova 3')
print x.getMsgs(18)

