1 - como identificar uma lista em python?

# para identifiar uma lista em python é preciso verificar se a variável é do tipo list, para isso podemos usar a função type() ou isinstance().
# Exemplo: if isinstance(variavel, list): print("É uma lista")

2 - como pegar o 1° elemento de uma lista em python?

# para pegar o 1° elemento de uma lista em python, basta usar o índice 0, pois os índices começam em 0. Exemplo: print(lista[0])

3 - como identificar um dicionário em python?

# para identificar um dicionário em python, basta verificar se a variável é do tipo dict, para isso podemos usar a função type() ou isinstance().
# Exemplo: if isinstance(variavel, dict): print("É um dicionário")

4 - como pegar um elemento em dicionário?

#  print(dicionario['chave'])

5 - como identfificar uma lista em dicionário?

# para identificar uma lista em um dicionário, basta verificar se o valor associado a uma chave é do tipo list, para isso podemos usar a função type() ou isinstance(). 
#Exemplo: if isinstance(dicionario['chave'], list): print("É uma lista")

6 - como teansformar uma lista de dicionário em um DataFrame?

# para transformar uma lista de dicionário em um DataFrame, tem que usar a função pd.DataFrame() do pandas, passando a lista de dicionário como argumento. 
# Exemplo: df = pd.DataFrame(lista_de_dicionarios)

7 - como consumir um arquivo csv no DataFrame?

# pd.read_csv() do pandas, passando o caminho do arquivo csv como argumento.

8 - como consumir um arquivo excel no DataFrame?

# pd.read_excel() do pandas, passando o caminho do arquivo excel como argumento.

9 - como filtrar uma coluna de valores?

# filtro = df['coluna'] > valor
# df[filtro]

10 - como filtrar uma coluna de string?

# filtro = df['coluna'] == 'string'