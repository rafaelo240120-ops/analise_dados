
#1 - Como identificar uma lista em Python?
pythonlista = ["rafael", 0, 50]

#2 - Como pegar o 1° elemento de uma lista em Python?
pythonlista[0]

#3 - Como identificar um dicionário em Python?
pythondicionario = {
    "nome": "rafael",
    "idade": 21,
    "endereco": "rua teste"
}

#4 - Como pegar um elemento em dicionário?
pythondicionario["nome"]

#5 - Como identificar uma lista de dicionário?
pythonlista2 = [dicionario]
lista2[0]

#6 - Como transformar uma lista de dicionário em um DataFrame?
pythonimport pandas as pd
df = pd.DataFrame(lista)
df = pd.DataFrame([dicionario])

#7 - Como consumir um arquivo CSV no DataFrame?
pythonarquivo = "notas.csv"
df = pd.read_csv(arquivo)

#8 - Como consumir um arquivo Excel no DataFrame?
pythonarquivo = "cadastro_alunos.xlsx"
df = pd.read_excel(arquivo)

#9 - Como filtrar uma coluna de valores inteiros?
pythonfiltro = df["national_rank"] > 4
df.loc[filtro, ["institution", "country"]]

#10 - Como filtrar uma coluna de string?
pythonfiltro = df["institution"].str.contains("^C")
df[filtro]