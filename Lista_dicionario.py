#. Exercício 1: Criando um Dicionário Crie um dicionário chamado 'aluno' com as seguintes chaves: 
#- 'nome': contendo um nome fictício, - 'idade': contendo a idade do aluno, - 'curso': contendo o curso que ele está matriculado. 
# Após criar o dicionário, exiba seus valores no seguinte formato: Nome: <nome> Idade: <idade> Curso: <curso>

aluno = {
    'nome': 'Rafael Augusto',
    'idade': 21,
    'curso': 'Ciências Econômicas'
}
print(f"Nome: {aluno['nome']} Idade: {aluno['idade']} Curso: {aluno['curso']}")

#2.0 : Manipulação de Dicionário
#Dado o dicionário abaixo:
#produto = {
    #"nome": "Teclado Mecânico",
    #"preco": 350.00,
    #"estoque": 10
#}
#2.1 Adicione uma nova chave chamada 'marca' com um valor de sua escolha.
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10,
    "marca": "Logitech"
}

#2.2. Atualize o preço do produto para R$ 320,00.

produto['preco'] = 320.00

#2.3. Reduza o estoque em 2 unidades.

produto['estoque'] -= 2

#2.4. Remova a chave 'marca' do dicionário.

del produto['marca']

#2.5. Exiba o dicionário atualizado.

print(produto)

#Exercício 3: Iterando sobre um Dicionário
#Dado o dicionário:
#notas = {
    #"Alice": 8.5,
    #"Bruno": 7.0,
    #"Carla": 9.2,
    #"Daniel": 6.8
#}
#3.1. Itere sobre o dicionário e exiba os nomes dos alunos e suas respectivas notas.
#notas = {
    #"Alice": 8.5,
    #"Bruno": 7.0,
    #"Carla": 9.2,
    #"Daniel": 6.8
#}

notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
for aluno, nota in notas.items():
    print(f"{aluno}: {nota}")

#3.2. Calcule a média das notas e exiba o resultado.

total_notas = sum(notas.values())
media = total_notas / len(notas)
print(f"Média das notas: {media}")

#Exercício 4: Soma de Valores
#Dado um dicionário com valores numéricos, percorra o dicionário e some todos os valores.
#Exemplo:
#numeros = {"a": 10, "b": 20, "c": 30}
#Saída esperada: 60

numeros = {"a": 10, "b": 20, "c": 30}
soma = sum(numeros.values())
print(f"Soma dos valores: {soma}")

#Exercício 5: Contagem de Itens Repetidos
#Dado uma lista de elementos, conte a frequência de cada elemento utilizando um dicionário.
#Exemplo:
#lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
#Saída esperada: {'maçã': 3, 'banana': 2, 'laranja': 1}

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
contagem = {}
for item in lista:
    contagem[item] = contagem.get(item, 0) + 1
print(contagem)

#Exercício 6: Filtrando Dicionário
#Dado um dicionário contendo produtos e seus preços, filtre os produtos que custam mais de R$ 50,00.
#Exemplo:
#produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
#Saída esperada: {"mochila": 80, "notebook": 3000}

produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
produtos_filtrados = {produto: preco for produto, preco in produtos.items() if preco > 50}
print(produtos_filtrados)

#Exercício 7: Tradutor Simples
#Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
#Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário.
#Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".

tradutor = {
    "hi": "oi",
    "bye": "tchau",
    "good morning": "bom dia",
    "deal": "negócio",
    "book": "livro"
}
palavra_ingles = input("Digite uma palavra em inglês: ")
traducao = tradutor.get(palavra_ingles)
if traducao:
    print(f"A tradução de '{palavra_ingles}' é '{traducao}'.")
else:    print("Palavra não encontrada.")


#Exercício 8: Lista de Compras
#Crie um dicionário onde as chaves são nomes de produtos e os valores são quantidades.
#Permita ao usuário adicionar produtos, atualizar quantidades e remover itens.
#No final, exiba a lista completa de compras.

lista_compras = {}
while True:
    acao = input("Digite 'adicionar', 'atualizar', 'remover' ou 'sair': ")
    if acao == 'sair':
        break
    elif acao == 'adicionar':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        lista_compras[produto] = lista_compras.get(produto, 0) + quantidade
    elif acao == 'atualizar':
        produto = input("Digite o nome do produto: ")
        if produto in lista_compras:
            quantidade = int(input("Digite a nova quantidade: "))
            lista_compras[produto] = quantidade
        else:
            print("Produto não encontrado.")
    elif acao == 'remover':
        produto = input("Digite o nome do produto: ")
        if produto in lista_compras:
            del lista_compras[produto]
        else:
            print("Produto não encontrado.")
    else:
        print("Ação inválida. Tente novamente.")



#Exercício 9: Dicionário Aninhado
#Crie um dicionário chamado 'turma' onde as chaves são nomes de alunos e os valores são dicionários contendo:
#- "idade" (inteiro),
#- "notas" (lista de três notas).
#Exemplo de estrutura:
#turma = {
#    "Ana": {"idade": 17, "notas": [8, 9, 7]},
#    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
#    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
#}
#1. Adicione um novo aluno ao dicionário.

turma = {
    "Lucas": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
turma["Victoria"] = {"idade": 18, "notas": [7, 8, 9]}

#2. Calcule a média de notas de cada aluno e exiba no formato:
#   Ana: Média 8.0
#   Pedro: Média 7.0
#   Mariana: Média 9.0

for aluno, dados in turma.items():
    media = sum(dados["notas"]) / len(dados["notas"])
    print(f"{aluno}: Média {media:.1f}")
    
#3. Encontre o aluno com a maior média e exiba o nome dele.
maior_media = 0
aluno_maior_media = ""
for aluno, dados in turma.items():
    media = sum(dados["notas"]) / len(dados["notas"])
    if media > maior_media:
        maior_media = media
        aluno_maior_media = aluno
print(f"Aluno com maior média: {aluno_maior_media} com média {maior_media:.1f}")


#Exercício 10: Cadastro de Funcionários
#Crie um programa que permita cadastrar funcionários em uma empresa.
#O programa deve permitir adicionar funcionários com os seguintes dados:
#- Nome
#- Cargo
#- Salário
#Os funcionários devem ser armazenados em um dicionário onde a chave é o nome e o valor é outro dicionário com os dados do funcionário.
#O programa deve permitir consultar funcionários pelo nome e exibir suas informações. 

funcionarios = {}
while True:
    acao = input("Digite 'adicionar', 'consultar' ou 'sair': ")
    if acao == 'sair':
        break
    elif acao == 'adicionar':
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        funcionarios[nome] = {"cargo": cargo, "salário": salario}
    elif acao == 'consultar':
        nome = input("Digite o nome do funcionário para consulta: ")
        if nome in funcionarios:
            info = funcionarios[nome]
            print(f"Nome: {nome}, Cargo: {info['cargo']}, Salário: R$ {info['salário']:.2f}")
        else:
            print("Funcionário não encontrado.")