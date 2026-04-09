

# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?
import pandas as pd
df = pd.read_csv(r"C:\Users\rafin\OneDrive\Documentos\Análise de dados\titanic.csv")

# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")
filtro = df["Sex"] == "female"
df_female = df[filtro]


# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")
filtro = df["Survived"] == 1
sobreviventes = df[filtro]


# Questão 4: Calcular a média da idade
# Quantos Homens Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived" e homens tem o valor "male" na coluna "Sex")
filtro = (df["Survived"] == 1) & (df["Sex"] == "male")  
homens_sobreviventes = df[filtro]
print(homens_sobreviventes)

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")
filtro = df["Name"].str.contains("John")
passageiros_john = df[filtro]