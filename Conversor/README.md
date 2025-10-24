# Conversor

Este projeto é um conversor entre números decimais e binários, permitindo que os usuários realizem conversões de forma interativa.

## Estrutura do Projeto

- `src/Conversor.py`: Contém as funções para conversão entre decimal e binário, além de uma interface interativa.
- `src/__main__.py`: Ponto de entrada do programa que inicia a interface interativa.
- `src/utils/__init__.py`: Organiza funções utilitárias que podem ser usadas em `Conversor.py` ou em outros módulos.
- `requirements.txt`: Lista as dependências do projeto.
- `pyproject.toml`: Configura o projeto, incluindo informações sobre dependências e configurações de build.
- `scripts/build_exe.sh`: Script para automatizar a criação de um executável a partir do código Python.
- `.gitignore`: Especifica arquivos ou pastas a serem ignorados pelo Git.

## Passo a Passo para Executar o Projeto

1. **Clone o repositório**:
   ```
   git clone <URL do repositório>
   cd Conversor
   ```

2. **Instale as dependências**:
   ```
   pip install -r requirements.txt
   ```

3. **Execute o programa**:
   ```
   python -m src
   ```

## Criando um Executável

Para criar um executável do programa, siga os passos abaixo:

1. **Dê permissão de execução ao script de build**:
   ```
   chmod +x scripts/build_exe.sh
   ```

2. **Execute o script de build**:
   ```
   ./scripts/build_exe.sh
   ```

3. **Encontre o executável na pasta `dist`** e execute-o diretamente.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.