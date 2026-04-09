x = 4
idade = 4
objeto = "palhaco"

lista = [objeto, idade, x]
lista[2]

lista_mista = [20, 30, 50, 10, "cavalo", "pato", 16, 17]
animal = []
numero = []

for item in lista_mista:
    if isinstance(item, str):
        animal.append(item)
    elif type(item) == int:
        numero.append(item)

dict_mista = {
    0: "cavalo",
    1: "pato",
    2: 20,
    3: 30,
    4: 50,
    5: 10,
    6: 16,
    7: 17
}
