dados = {'nome':"Gabriel", 'cpf':"133.66.464-58", 'cidade':"surubim", 'nascimento':"06-10-2003"}
dados['sexo']='masculino'
print(dados['sexo'])


extra = {'altura': "1.90", 'peso':"59kg"}

print(dados)
print("-" * 10)
print(extra)
print("#" * 30)


#concatenar / juntar os dois dicionarios
final = {**dados , **extra} ## ou dados.update(extra)
print(final)

"""for chave in dados:
    print(f'chave -> {chave} / valor -> {final[chave]}')"""

for chave , valor in final.items():
    print(f'chave -> {chave} / valor -> {valor}')