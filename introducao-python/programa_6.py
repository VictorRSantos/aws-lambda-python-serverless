# Descrição:  string

nome = 'Tony'
sobrenome = 'Stark'

nome_completo = nome + ' ' + sobrenome
print(nome)
print(sobrenome)
print(nome_completo)

congratulacao = "Feliz"
situacao_1 = 'Natal'
situacao_2 = 'Ano novo'

mensagem_1 = f'Tenha um {congratulacao} dia de {situacao_1}'
mensagem_2 = f'Tenha um {congratulacao} dia de {situacao_2}'

print(mensagem_1)
print(mensagem_2)

versao = 'ABC123'
versao += '-10'
print(versao)

existe_feliz = 'Feliz' in mensagem_1
print(existe_feliz)

existe_infeliz = 'Infeliz' in mensagem_1
print(existe_infeliz)

print(mensagem_1[6])
print(mensagem_1[0:6])
print(mensagem_1[9:15])

print('ABC')
print('Abc'.lower())
print('Abc'.upper())

print('Abc'.find('b'))
print('Abc'.replace('b', 'x'))