## Manipulador de pdfs em Python

Este é  um projeto em Python que permite extrair e combinar ficheiros PDF e adicionar marca de água a páginas selecionadas. 
O script permite fazer a seleção de páginas específicas de múltiplos PDFs, combinar essas páginas em um único PDF e por fim adicionar uma marca de água ao PDF final.

## Estrutura do projeto

Na pasta "Manipular_pdfs" é possível encontrar uma pasta "manipulador_utils" que engloba 3 ficheiros python:


- __init__.py: ficheiro  que permite importar módulos 

- manipulador.py: ficheiro que contém a class ManipulatorPDF e onde se encontram definidas funções base para o main script.

- pdfs.py: Onde se encontra a localização dos pdfs e as páginas selecionadas dos pdfs a serem usadas. 
O script recebe uma estrutura de dados em dicionário, onde:
    -  A chave é o nome do arquivo PDF
    - O valor é uma lista com os índices das páginas desejadas;

E ainda 2 ficheiros:

- main.py: Ficheiro que tem por base o script do projeto.

- README.md: Ficheiro-resumo do projeto e objetivos do mesmo.


## Como correr o projeto

1. Abrir um terminal
2. Ir até à pasta do projeto
3. Instalar biblioteca PyPDF2
```bash
pip install PyPDF2
```
4. Executar o script
```bash
python main.py
```

## Dependências

Instalação e importação da biblioteca PyPDF2
```bash
pip install PyPDF2
```

## Próximos passos/ Sugestões

Adicionar/ extrair imagens de pdfs(?)
Eliminar páginas de pdfs(?)