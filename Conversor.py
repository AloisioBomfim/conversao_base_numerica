import tkinter as tk
from tkinter import ttk, messagebox

# =========================
# Funções de conversão
# =========================

# Converte decimal para binário, incluindo parte fracionária
def decimal_para_binario(n, casas=10):
    parte_inteira = int(n)
    parte_fracionaria = n - parte_inteira
    bin_inteira = bin(parte_inteira)[2:]
    bin_fracionaria = ""
    count = 0
    while parte_fracionaria > 0 and count < casas:
        parte_fracionaria *= 2
        bit = int(parte_fracionaria)
        bin_fracionaria += str(bit)
        parte_fracionaria -= bit
        count += 1
    return f"{bin_inteira}.{bin_fracionaria}" if bin_fracionaria else bin_inteira

# Converte binário (com ou sem parte fracionária) para decimal
def binario_para_decimal(b):
    if '.' in b:
        parte_inteira, parte_frac = b.split('.')
    else:
        parte_inteira, parte_frac = b, ''
    decimal = int(parte_inteira, 2)
    for i, bit in enumerate(parte_frac, 1):
        decimal += int(bit) * (2 ** -i)
    return decimal

# Conversões diretas entre bases inteiras
def decimal_para_octal(n):
    return oct(int(n))[2:]

def octal_para_decimal(o):
    return int(o, 8)

def decimal_para_hex(n):
    return hex(int(n))[2:].upper()

def hex_para_decimal(h):
    return int(h, 16)

# Conversões indiretas via decimal
def binario_para_octal(b):
    return decimal_para_octal(binario_para_decimal(b))

def octal_para_binario(o):
    return decimal_para_binario(octal_para_decimal(o))

def binario_para_hex(b):
    return decimal_para_hex(binario_para_decimal(b))

def hex_para_binario(h):
    return decimal_para_binario(hex_para_decimal(h))

# =========================
# Função principal de conversão
# =========================

def converter():
    origem = origem_var.get()
    destino = destino_var.get()
    entrada = entrada_var.get().strip()
    casas = casas_var.get()

    # Verifica se as bases são iguais
    if origem == destino:
        messagebox.showwarning("Bases iguais", "As bases de origem e destino devem ser diferentes.")
        return

    try:
        casas = int(casas) if casas else 10

        # Conversões a partir da base de origem
        if origem == "Decimal":
            valor = float(entrada.replace(",", "."))
            if destino == "Binário":
                resultado = decimal_para_binario(valor, casas)
            elif destino == "Octal":
                resultado = decimal_para_octal(valor)
            elif destino == "Hexadecimal":
                resultado = decimal_para_hex(valor)

        elif origem == "Binário":
            if not all(c in "01." for c in entrada):
                raise ValueError("Binário inválido.")
            if destino == "Decimal":
                resultado = binario_para_decimal(entrada)
            elif destino == "Octal":
                resultado = binario_para_octal(entrada)
            elif destino == "Hexadecimal":
                resultado = binario_para_hex(entrada)

        elif origem == "Octal":
            if destino == "Decimal":
                resultado = octal_para_decimal(entrada)
            elif destino == "Binário":
                resultado = octal_para_binario(entrada)
            elif destino == "Hexadecimal":
                decimal = octal_para_decimal(entrada)
                resultado = decimal_para_hex(decimal)

        elif origem == "Hexadecimal":
            if destino == "Decimal":
                resultado = hex_para_decimal(entrada)
            elif destino == "Binário":
                resultado = hex_para_binario(entrada)
            elif destino == "Octal":
                decimal = hex_para_decimal(entrada)
                resultado = decimal_para_octal(decimal)

        else:
            resultado = "Conversão não suportada."

        # Exibe o resultado na interface
        resultado_var.set(f"Resultado: {resultado}")

    except Exception as e:
        # Exibe mensagem de erro em caso de entrada inválida
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# =========================
# Interface gráfica com Tkinter
# =========================

# Criação da janela principal
root = tk.Tk()
root.title("Conversor Numérico Multibase - Criado por Aloisio Bomfim")
root.geometry("500x300")  # Tamanho ajustado para acomodar os elementos

# Lista de bases disponíveis
bases = ["Decimal", "Binário", "Octal", "Hexadecimal"]

# Variáveis de controle da interface
origem_var = tk.StringVar()
destino_var = tk.StringVar()
entrada_var = tk.StringVar()
casas_var = tk.StringVar()
resultado_var = tk.StringVar()

# Elementos da interface
ttk.Label(root, text="Base de origem:").grid(column=0, row=0, padx=10, pady=5, sticky="w")
ttk.Combobox(root, textvariable=origem_var, values=bases, state="readonly").grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Base de destino:").grid(column=0, row=1, padx=10, pady=5, sticky="w")
ttk.Combobox(root, textvariable=destino_var, values=bases, state="readonly").grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Número:").grid(column=0, row=2, padx=10, pady=5, sticky="w")
ttk.Entry(root, textvariable=entrada_var).grid(column=1, row=2, padx=10, pady=5)

ttk.Label(root, text="Casas decimais (se aplicável):").grid(column=0, row=3, padx=10, pady=5, sticky="w")
ttk.Entry(root, textvariable=casas_var).grid(column=1, row=3, padx=10, pady=5)

ttk.Button(root, text="Converter", command=converter).grid(column=0, row=4, columnspan=2, pady=10)

# Resultado com fonte ampliada para destaque
resultado_label = ttk.Label(root, textvariable=resultado_var, foreground="blue")
resultado_label.grid(column=0, row=5, columnspan=2, pady=10)
resultado_label.config(font=("Arial", 20))  # Tamanho da fonte ajustado

# Inicia o loop da interface
root.mainloop()