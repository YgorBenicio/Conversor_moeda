def converter_moeda(valor, taxa_cambio, inverso=False):
    # Se a conversão for inversa, multiplica o valor pela taxa
    if inverso:
        return valor * taxa_cambio
    # Caso contrário, divide o valor pela taxa
    return valor / taxa_cambio

# Mostra o menu de opções
print("Conversor de Moeda")
print("1. Real para Dólar")
print("2. Real para Euro")
print("3. Real para Iene")
print("4. Real para Peso")
print("5. Dólar para Real")
print("6. Euro para Real")
print("7. Iene para Real")
print("8. Peso para Real")

# Pede para o usuário escolher uma opção
opcao = int(input("Escolha a opção de conversão: "))

# Pede para o usuário digitar o valor a ser convertido
valor = float(input("Digite o valor a ser convertido: "))

# Pede para o usuário digitar a taxa de câmbio
taxa = float(input("Digite a taxa de câmbio: "))

# Verifica se a opção escolhida é válida
if opcao >= 1 and opcao <= 8:
    # Se a opção for 5, 6, 7 ou 8, a conversão é inversa
    # Isso significa que está convertendo de uma moeda estrangeira para Real
    if opcao > 4:
        inverso = True
    else:
        # Caso contrário, está convertendo de Real para uma moeda estrangeira
        inverso = False
    
    # Faz a conversão usando a função
    resultado = converter_moeda(valor, taxa, inverso)
    
    # Mostra o resultado da conversão
    print(f"{valor} na moeda de origem é igual a {resultado:.2f} na moeda de destino")
else:
    # Se a opção for inválida, mostra uma mensagem de erro
    print("Opção inválida")