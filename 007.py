import os
import re
import shutil

print("Cole um path absoluto!")
fish = input("--> : ")

#direciona o local para o projeto
os.chdir(fish)

pato = os.getcwd() + '/'

#listas
dires = os.listdir()
pastas = []
arquivos = []

#separa as pastas dos arquivos
for dire in dires:
    if os.path.isfile(dire):
        arquivos.append(dire)
    elif os.path.isdir(dire):
        pastas.append(dire)

#verifica se presisa criar pastas
import sete
for dire1 in sete.spam:
    x = pastas.count(dire1)
    if x == 0:
        os.makedirs(dire1)
        print(dire1)

#localizar files e mover para a pasta?

padrao = re.compile(r'\.\w+$')

for arquivo in arquivos:
    p1 = padrao.search(arquivo)
    pg = p1.group()
    pg = pg.replace(".","")
    if pg in sete.spam:
        start = pato + arquivo
        fim = pato + pg
        shutil.move(start,fim)
