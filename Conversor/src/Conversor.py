# filepath: c:\Conversor\src\Conversor.py
def decimal_para_binario(numero_decimal, casas_fracionarias=10):
    parte_inteira = int(numero_decimal)
    parte_fracionaria = numero_decimal - parte_inteira

    bin_inteira = bin(parte_inteira)[2:]

    bin_fracionaria = ""
    contador = 0
    while parte_fracionaria > 0 and contador < casas_fracionarias:
        parte_fracionaria *= 2
        bit = int(parte_fracionaria)
        bin_fracionaria += str(bit)
        parte_fracionaria -= bit
        contador += 1

    if bin_fracionaria:
        return f"{bin_inteira}.{bin_fracionaria}"
    else:
        return bin_inteira


def binario_para_decimal(binario_str):
    if '.' in binario_str:
        parte_inteira_str, parte_fracionaria_str = binario_str.split('.')
    else:
        parte_inteira_str = binario_str
        parte_fracionaria_str = ''

    decimal_inteira = int(parte_inteira_str, 2)

    decimal_fracionaria = 0
    for i, bit in enumerate(parte_fracionaria_str, start=1):
        decimal_fracionaria += int(bit) * (2 ** -i)

    return decimal_inteira + decimal_fracionaria


def main():
    # 🌟 Interface interativa
    print("🔁 Conversor Binário ↔ Decimal")
    print("Escolha a operação:")
    print("1 - Decimal para Binário")
    print("2 - Binário para Decimal")

    opcao = input("Digite 1 ou 2: ").strip()

    if opcao == "1":
        entrada = input("\nDigite um número decimal (ex: 27.58): ")
        try:
            numero = float(entrada.replace(",", "."))
            casas = input("Quantas casas decimais deseja no binário? (padrão: 10): ")
            casas = int(casas) if casas.strip() else 10
            binario = decimal_para_binario(numero, casas)
            print(f"\n✅ Resultado: {numero} em binário é {binario}")
        except ValueError:
            print("❌ Entrada inválida. Certifique-se de digitar um número decimal.")
    elif opcao == "2":
        entrada = input("\nDigite um número binário (ex: 10001.1): ")
        try:
            if not all(c in "01." for c in entrada):
                raise ValueError
            decimal = binario_para_decimal(entrada)
            print(f"\n✅ Resultado: {entrada} em decimal é {decimal}")
        except ValueError:
            print("❌ Entrada inválida. Certifique-se de digitar um número binário válido.")
    else:
        print("❌ Opção inválida. Escolha 1 ou 2.")

if __name__ == "__main__":
    main()