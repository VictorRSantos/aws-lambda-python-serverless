# Tipos dados Dicionarios

gato_1 = dict(nome = 'Obi-Wan', idade=2)
gato_2 = {'nome':'Obi-Wan', 'idade':2}
print(type(gato_1))
print(type(gato_2))
print(gato_1)
print(gato_2)

carro_1 = {
    'cor':'cinza',
    'ano':2023,
    'modelo':'Fusca',
    'marca':'Volkswagen',
    'ipva':True
}

print(carro_1)
print(carro_1['marca'])
print(carro_1['cor'])
print('tanque' in carro_1)

print(len(carro_1))

del carro_1['marca']
# print(carro_1['marca'])
print(len(carro_1))
print(list(carro_1))

carro_1['ano'] = 2007
print(carro_1['ano'])

