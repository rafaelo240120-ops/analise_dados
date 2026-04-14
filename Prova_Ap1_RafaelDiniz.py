import pandas as pd
import requests
import yfinance

df = pd.read_csv(r"C:\Users\rafin\OneDrive\Documentos\Análise de dados\ncr_ride_bookings.csv")
df 


# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento

# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 

filtro = df["Booking Status"] == "Completed"

filtro = df["Booking Status"].str.contains("Completed", case=False) 


# (0,5) 2 - Qual a proporção em relação ao total de corridas?



# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.

df.groupby("Vehicle Type")["Ride Distance"].mean()

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?

filtro2 = df["PaymentMethod"] == "Bike"

df["PaymentMethod_Bike"] = df["Payment Method"] == "Bike"
df["rank_PaymentMethod_Bike"] = df["PaymentMethod_Bike"].rank(ascending=False)
PMB = df.sort_values("rank_PaymentMethod_Bike").head(10)


# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?

filtro3 = df["Booking Value"] == "Completed"

# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?

df["booking_status_completed"] = df["Booking Status"].str.contains("Completed", case=False) 
df.groupby("booking_status_completed")["Booking Value"].mean()



# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;

import requests
import pandas as pd
url = "https://www.ipeadata.gov.br/api/odata4/Metadados/"
response = requests.get(url)
response.status_code
dados = response.json()
dados = dados["value"]
df = pd.DataFrame(dados)
df = df.loc[:,["SERNOME","FNTSIGLA",]]
df

# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.

CODIGO ENCONTRADO = ''


# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
 #response = requests.get(
  #   f"{base_url}/preco/corrigido",
   #  headers={"Authorization": f"Bearer {token}"},
    # params=params,
 )

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzcwMzE1MCwiaWF0IjoxNzc2MTY3MTUwLCJqdGkiOiJhYTdkNzVhNTJmNjA0ODMwYTg5ZDc4ZTIwNTIzNjYxZiIsInVzZXJfaWQiOiI5OSJ9.JQfsaGxQwW-cO2ZfcOb1Wv-yqMTG4E3m6cmn8z0ugEI"
params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
 response = requests.get(
     f"{base_url}/preco/corrigido",
     headers={"Authorization": f"Bearer {token}"},
     params=params,
 )
df_preco = pd.DataFrame(response.json())

preco_ini = float(df_preco["fechamento"].iloc[0])
preco_fim = float(df_preco["fechamento"].iloc[-1])

retorno = (preco_fim / preco_ini - 1) * 100





# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
 base_url = "https://laboratoriodefinancas.com/api/v2"
 token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzcwMzE1MCwiaWF0IjoxNzc2MTY3MTUwLCJqdGkiOiJhYTdkNzVhNTJmNjA0ODMwYTg5ZDc4ZTIwNTIzNjYxZiIsInVzZXJfaWQiOiI5OSJ9.JQfsaGxQwW-cO2ZfcOb1Wv-yqMTG4E3m6cmn8z0ugEI"
 response = requests.get(
     f"{base_url}/bolsa/planilhao",
     headers={"Authorization": f"Bearer {token}"},
     params={"data_base": "2026-04-01"},
 )

df1 = pd.DataFrame(response.json())

 df2 = df1[["ticker", "setor", "roe"]]
df2

df2['rank_roe'] = df2['roe'].rank(ascending=False)
df2['rank_setor'] = df2['setor'].rank(ascending=False)

df2['rank_final'] = (df2['rank_roe'] + df2['rank_setor']) / 2

maior_roe_tec = df2.sort_values('rank_final', ascending=False)['ticker'][:1]


# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

base_url = "https://laboratoriodefinancas.com/api/v2"
 token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzcwMzE1MCwiaWF0IjoxNzc2MTY3MTUwLCJqdGkiOiJhYTdkNzVhNTJmNjA0ODMwYTg5ZDc4ZTIwNTIzNjYxZiIsInVzZXJfaWQiOiI5OSJ9.JQfsaGxQwW-cO2ZfcOb1Wv-yqMTG4E3m6cmn8z0ugEI"
 response = requests.get(
     f"{base_url}/bolsa/planilhao",
     headers={"Authorization": f"Bearer {token}"},
     params={"data_base": "2026-04-01"},
 )

df1 = pd.DataFrame(response.json())

 df2 = df1[["ticker", "earning_yield", "roc"]]
df2

df2['rank_roc'] = df2['roc'].rank(ascending=False)
df2['rank_earning_yield'] = df2['earning_yield'].rank(ascending=False)

df2['rank_final_magic'] = (df2['rank_roc'] + df2['rank_earning_yield']) / 2

Carteira_Magic = df2.sort_values('rank_final_magic', ascending=False)['ticker'][:10]




# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?

df3 = Carteira_Magic[["setor"]]
