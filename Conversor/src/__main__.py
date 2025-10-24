def main():
    from Conversor import decimal_para_binario, binario_para_decimal

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