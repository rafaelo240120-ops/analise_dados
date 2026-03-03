
import pandas as pd
df = pd.read_excel(r"C:\Users\rafin\Downloads\salary.xlsx")
df.shape
df.columns
df.dtypes
df.isnull().sum()

#1.	Quantas linhas e quantas colunas tem o dataset?

df.shape

#2.	Qual a média salarial? Qual é o maior salário? O menor salário?
media_salarial = df['salary'].mean()
maior_salario = df['salary'].max()
menor_salario = df['salary'].min()
print(f"Média Salarial: {media_salarial}")
print(f"Maior Salário: {maior_salario}")
print(f"Menor Salário: {menor_salario}")    


#3.	Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio?

df[['job_title', 'salary', 'company_location', 'company_size', 'remote_ratio']]

#4.	Qual é o maior e menor salário de um “Data Scientist”? Onde fica essas empresas?

filtro = df['job_title'] == 'Data Scientist'
df.loc[filtro, ['job_title', 'salary', 'company_location']].sort_values('salary')

#5.	Qual a profissão com a maior média salarial? E a menor?

df.groupby('job_title')['salary'].mean().sort_values()

#6.	Quais as profissões com a média salarial maior que a média geral?

media_geral = df['salary'].mean()   
filtro = df.groupby('job_title')['salary'].mean() > media_geral
profissoes_acima_media = df.groupby('job_title')['salary'].mean()[filtro
].index
profissoes_acima_media

#7.	Qual a localização com maior média salarial?

df.groupby('company_location')['salary'].mean().sort_values(ascending=False).head(1)

#8.	Quais as profissões que existem no Brasil (BR)?
filtro = df['company_location'] == 'BR'
df.loc[filtro, 'job_title'].unique()
#9.	Qual a média salarial no Brasil?
df.loc[filtro, 'salary'].mean()
#10.	Quantas profissões existem no Brasil?
df.loc[filtro, 'job_title'].nunique()

#11.	Qual a profissão que mais ganha no Brasil?

df.loc[filtro].groupby('job_title')['salary'].max().sort_values(ascending=False).head(1)

#12.	Quantas profissões tem nos US e que trabalham em empresas grandes (L)?

filtro = (df['company_location'] == 'US') & (df['company_size'] == 'L')
df.loc[filtro, 'job_title'].nunique()

#13.	Qual é a média salarial das empresas médias (M) na Canada (CA)?

filtro = (df['company_location'] == 'CA') & (df['company_size'] == 'M')
df.loc[filtro, 'salary'].mean()

#14.	Qual é o país com mais profissões? E qual é o mais com menos?

df.groupby('company_location')['job_title'].nunique().sort_values(ascending=False).head(1)
df.groupby('company_location')['job_title'].nunique().sort_values(ascending=True).head(1)

#15.	Quem ganha mais que trabalha remoto, presencial ou híbrido?

df.groupby('remote_ratio')['salary'].mean().sort_values(ascending=False)
    
#16.	Qual o país com maior numero de profissões trabalhando 100% remoto?

filtro = df['remote_ratio'] == 100 
df.loc[filtro].groupby('company_location')['job_title'].nunique().sort_values(ascending=False).head(1)
