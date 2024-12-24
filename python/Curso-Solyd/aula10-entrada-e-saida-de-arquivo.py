arquivo = open('arquivo.txt', 'w')
'''
-r server para ler , -a append, -b abertura em byte
'''
for i in range(0, 1000):
    arquivo.write(str(i)+'\n')