arquivo = open('arquivo.txt', 'a')
'''
-r server para ler , -a append, -b abertura em byte
'''
for i in range(0, 999):
  arquivo.write(str(i)+'\n')
