#!/bin/bash

# Este script automatiza o processo de criação de um executável a partir do código Python usando PyInstaller.

# Verifica se o PyInstaller está instalado
if ! command -v pyinstaller &> /dev/null
then
    echo "❌ PyInstaller não está instalado. Instale-o usando 'pip install pyinstaller'."
    exit 1
fi

# Cria o executável
echo "🔄 Criando o executável..."
pyinstaller --onefile src/__main__.py

# Verifica se o processo foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "✅ Executável criado com sucesso na pasta 'dist'."
else
    echo "❌ Ocorreu um erro ao criar o executável."
fi