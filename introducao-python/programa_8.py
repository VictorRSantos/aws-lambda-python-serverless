# Tipos Booleanos

ec2_ligado = True
rds_ligado = False

print(f'A instância ec2 está ligada? {ec2_ligado}')
print(f'O banco de dados está ligada? {rds_ligado}')

print(not True)
print(not False)


print(ec2_ligado and rds_ligado)
print(ec2_ligado or rds_ligado)