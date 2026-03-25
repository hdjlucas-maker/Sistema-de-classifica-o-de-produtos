produtos = []

while True:
    nome = input("Nome do produto: ")
    
    try:
        preco = float(input("Preço: R$ "))
    except ValueError:
        print("Digite um número válido pro preço.")
        continue

    # Classificação
    if preco <= 9.99:
        categoria = "Barato"
    elif preco <= 200:
        categoria = "Médio"
    else:
        categoria = "Caro"

    produtos.append((nome, preco, categoria))

    continuar = input("Cadastrar outro produto? (s/n): ")
    if continuar.lower() != "s":
        break

# Relatório final
print("\n--- RELATÓRIO DE PRODUTOS ---")

barato = medio = caro = 0

for p in produtos:
    print(f"Produto: {p[0]} | Preço: R$ {p[1]:.2f} | Categoria: {p[2]}")

    if p[2] == "Barato":
        barato += 1
    elif p[2] == "Médio":
        medio += 1
    else:
        caro += 1

print("\n--- RESUMO ---")
print(f"Total de produtos: {len(produtos)}")
print(f"Baratos: {barato}")
print(f"Médios: {medio}")
print(f"Caros: {caro}")

# Dica de venda automática
print("\n--- ANÁLISE ---")
if caro > medio:
    print("Você tem muitos produtos caros. Tente criar ofertas ou parcelamento.")
elif medio > barato:
    print("Boa! Produtos médios são os que mais vendem.")
else:
    print("Use produtos baratos para atrair clientes e vender mais.")
