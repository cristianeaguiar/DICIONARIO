# tupla
campos = ("Nome", "Idade", "Profissão", "E-mail")

# dicionário
usuario = {}

#entrada de dados
for campo in campos:
    usuario[campo] = input(f"Informe o valor do campo {campo}: ") 

#exibe os valores do dicionário na tela
print("DADOS DO USUÁRIO:\n")
for campo in campos:
    print(f"{campo}: {usuario.get(campo)}.")



