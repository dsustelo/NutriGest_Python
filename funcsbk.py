import openpyxl

class Ingrediente:
    def __init__(self, nome, codigo, calorias, kj, agua, proteina, lipidos, carboidratos, acucar):
        self.nome = nome
        self.calorias = calorias
        self.proteina = proteina
        self.carboidratos = carboidratos
        self.acucar = acucar


class Prato:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []

    def adicionar_ingrediente(self, ingrediente, quantidade):
        self.ingredientes.append({"ingrediente": ingrediente, "quantidade": quantidade})

    def calcular_valor_nutricional(self):
        total_calorias = 0
        total_proteina = 0
        total_carboidratos = 0
        total_acucar = 0

        for item in self.ingredientes:
            ingrediente = item["ingrediente"]
            quantidade = item["quantidade"]

            total_calorias += ingrediente.calorias * quantidade
            total_proteina += ingrediente.proteina * quantidade
            total_carboidratos += ingrediente.carboidratos * quantidade
            total_acucar += ingrediente.acucar * quantidade

        return {
            "calorias": total_calorias,
            "proteina": total_proteina,
            "carboidratos": total_carboidratos,
            "acucar": total_acucar,
        }


# Carregar dados do Excel
wb = openpyxl.load_workbook('TabelaNutri.xlsx')
sheet = wb.active

# Criar dicionário de ingredientes
ingredientes_dict = {}
for row in sheet.iter_rows(min_row=4, values_only=True):
    codigo, nome, calorias, kj, agua, proteina, lipidos, carboidratos, acucar = row
    ingredientes_dict[nome] = Ingrediente(nome, codigo, calorias, kj, agua, proteina, lipidos, carboidratos, acucar)

# Exemplo de uso
prato1 = Prato("Salada")
prato1.adicionar_ingrediente(ingredientes_dict["Alface"], 1.5)
prato1.adicionar_ingrediente(ingredientes_dict["Tomate"], 1)

valor_nutricional_salada = prato1.calcular_valor_nutricional()

print(f"Valor Nutricional da {prato1.nome}:")
print(f"Calorias: {valor_nutricional_salada['calorias']} kcal")
print(f"Proteína: {valor_nutricional_salada['proteina']} g")
print(f"Carboidratos: {valor_nutricional_salada['carboidratos']} g")
print(f"Acucar: {valor_nutricional_salada['acucar']} g")
