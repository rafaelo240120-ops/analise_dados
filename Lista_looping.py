
#1.	Crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja", "uva".

maca = "maçã"
banana = "banana"
laranja = "laranja"
uva = "uva"

frutas = [maca, banana, laranja, uva]

#2.	Imprima o primeiro e o último elemento da lista.

print(frutas[0])
print(frutas[3])

#3.	Adicione a fruta "manga" ao final da lista frutas.

manga = "manga" 
frutas.append(manga)
frutas = [maca, banana, laranja, uva, manga]

#4.	Remova a fruta "banana" da lista frutas.

frutas.remove("banana")
frutas = [maca, laranja, uva, manga]

#5.	Substitua Laranaja por Abacaxi na lista frutas.

frutas[1] = "abacaxi"
frutas = [maca, "abacaxi", uva, manga]

#6.	Crie uma lista de números inteiros de 1 a 10.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#7.	Calcule e imprima a soma de todos os números na lista.

soma = sum(numeros)
print(soma)

#8. Encontre e imprima o maior e o menor número na lista.

maior = max(numeros)
menor = min(numeros)
print(f"O maior número é {maior} e o menor número é {menor}.")

9#. Inverta a ordem dos elementos na lista de números e imprima a lista invertida.

numeros_invertidos = numeros[::-1]

10#. Crie uma lista cidades contendo as seguintes cidades: "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba". 

sao_paulo = "São Paulo"
rio_de_janeiro = "Rio de Janeiro"
belo_horizonte = "Belo Horizonte"
curitiba = "Curitiba"
cidades = [sao_paulo, rio_de_janeiro, belo_horizonte, curitiba]

11#. Imprima a lista de cidades em ordem alfabética.

cidades_ordenadas = sorted(cidades)
print(cidades_ordenadas)

12#. Adicione a cidade "Porto Alegre" ao final da lista cidades.

porto_alegre = "Porto Alegre"
cidades.append(porto_alegre)
cidades = [sao_paulo, rio_de_janeiro, belo_horizonte, curitiba, porto_alegre]

13#. Encontre o indice da cidade "Curitiba" na lista cidades.

indice_curitiba = cidades.index("Curitiba")

14#. Remova a cidade "Rio de Janeiro" da lista cidades.

cidades.remove("Rio de Janeiro")
cidades = [sao_paulo, belo_horizonte, curitiba, porto_alegre]

15#. Crie duas listas lista1 e lista2, onde lista1 contém os números 1, 2, 3 e lista2 contém os números 4, 5, 6.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

16#. COncatene as duas listas lista1 e lista2 em uma nova lista chamada lista3.

lista3 = lista1 + lista2

17#. Imprima a lista3.

print(lista3)

18#. Crie duas listas animais_domesticos e animais_silvestres, onde animais_domesticos contém os animais "cachorro", "gato" e "coelho", e animais_silvestres contém os animais "leão", "tigre" e "urso".

cachorro = "cachorro"
gato = "gato"
coelho = "coelho"
leao = "leão"
tigre = "tigre"
urso = "urso"
animais_domesticos = [cachorro, gato, coelho]
animais_silvestres = [leao, tigre, urso]

19#. Concatene as duas listas em nova lista todos_animais.

todos_animais = animais_domesticos + animais_silvestres

20#. Imprima todos_animais.

print(todos_animais)

21#. Crie uma lista nomes contendo os nomes: Ana, Pedro, Maria, João.

nomes = ["Ana", "Pedro", "Maria", "João"]

22#. Crie um loop for para imprimir cada nome na lista.

for nome in nomes:
    print(nome)

23#. Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas usando um loop for.

nomes_maiusculos = []
for nome in nomes:
    nomes_maiusculos.append(nome.upper())
print(nomes_maiusculos)

24#. Crie uma nova lista numeros contendo de 1 a 20. Utilize um loop para imprimir apenas os números pares.

numeros = list(range(1, 21))
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print(pares)

25#. Usando a lista numeros , uilize um loop para criar uma nova lista quadrados contendo o quadrado de cada número na lista.

quadrados = []
for num in numeros:
    quadrados.append(num ** 2)
print(quadrados)

26#. Crie uma lista palavras contendo as seguintes palavras: "python", "java", "c", "javascript". Utilize um loop for para imprimir o tamanho (Numero de letras) de cada palavra.

palavras = ["python", "java", "c", "javascript"]
for palavra in palavras:
    print(f"A palavra '{palavra}' tem {len(palavra)} letras.")

27#. Crie uma lista idades contendo [12, 18, 25, 40, 60]. Utilize um loop for para imprimir "maior de idade"se a idade for >= 18 e "menor de idade" se a idade for < 18.

idades = [12, 18, 25, 40, 60]
for idade in idades:
    if idade >= 18:
        print(f"{idade} é maior de idade.")
    else:
        print(f"{idade} é menor de idade.")

28#. Crie uma lista notas contendo [5.5, 7.0, 8.3, 4.9, 6.2]. Utilize um loop for para contar quantos alunos estao aprovados (nota >= 7.0) e quantos estão reprovados (nota < 7.0).

notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
reprovados = 0
for nota in notas:
    if nota >= 7.0:
        aprovados += 1
    else:
        reprovados += 1
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos reprovados: {reprovados}")

29#. Crie uma lista compras com [ärroz", "feijão", "batata", "carne"]. Utilize um loop for para imprimir cada item precedido da frase "Preciso comprar".

compras = ["arroz", "feijão", "batata", "carne"]
for item in compras:
    print(f"Preciso comprar {item}.")   


30#. Escreva um programa que use um loop while para imprimir os numeros de 1 a 10.

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

31#. Usando um loop while, peca para o usuario digitar um numero inteiro. O programa deve parar quando o usuario digitar o numero 0.

while True:
    numero = int(input("Digite um número inteiro (0 para parar): "))
    if numero == 0:
        print("Programa encerrado.")
        break
    else:
        print(f"Você digitou: {numero}")


32#. Utilize um loop while para calcular a soma dos numeros de 1 a 100.

soma = 0
contador = 1
while contador <= 100:
    soma += contador
    contador += 1
print(f"A soma dos números de 1 a 100 é: {soma}")

33#. Peca para o usuario advinhar um numero secreto por exemplo o 7. Use um loop while para continuar pedindo ate que ele acerte. 

numero_secreto = 7
while True:
    palpite = int(input("Adivinhe o número secreto (entre 1 e 10): "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto.")
        break
    else:
        print("Tente novamente!")

34#. Crie um loop while que imprima todos os numero pares de 2 ate 20.

contador = 2
while contador <= 20:
    print(contador)
    contador += 2


