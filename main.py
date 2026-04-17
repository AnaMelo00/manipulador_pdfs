#Instalar PyPDF2
#Importar PyPDF2 

#Criar função que leia um pdf e retorne um objeto PyPDF2.PdfReader. Trata erros caso o arquivo não exista/seja inválido

import os
from PyPDF2 import PdfReader, PdfWriter

def ler_pdf(arquivo_pdf):
    
    if not os.path.isfile(arquivo_pdf):
        print(f"Erro: Arquivo '{arquivo_pdf}' não encontrado.")
        return None

    try:
        with open(arquivo_pdf, "rb") as f:
            reader = PyPDF2.PdfReader(f)
 # Tenta abrir a primeira página para validar o PDF
            _ = reader.pages[0]
            return reader
    except Exception as e:
        print(f"Erro ao ler '{arquivo_pdf}': {e}")
        return None
    

# Validar se o índice é um número inteiro não-negativo

    def validar_indice(indice):
    
        if not isinstance(indice, int):
            print(f"Aviso: Índice '{indice}' não é um número inteiro e será ignorado.")
            return False
        if indice < 0:
            print(f"Aviso: Índice '{indice}' é negativo e será ignorado.")
            return False
        return True
    



def combinar_pdfs(pdfs_paginas, output_path, watermark_path=None, paginas_com_marca=None):

    writer = PdfWriter()

    # Combinar as páginas 
    for pdf_file, paginas in pdfs_paginas.items():
        try:
            reader = PdfReader(pdf_file)
            for idx in paginas:
                if idx < len(reader.pages):
                    page = reader.pages[idx]
                    writer.add_page(page)
                else:
                    print(f"Aviso: página {idx} não existe em {pdf_file}.")
        except FileNotFoundError:
            print(f"Erro: Arquivo {pdf_file} não encontrado.")

    # Se existir marca de água
    if watermark_path:
        watermark_reader = PdfReader(watermark_path)
        watermark_page = watermark_reader.pages[0]  
        # Marca de água geralmente tem uma página só

        for i, page in enumerate(writer.pages):
            if paginas_com_marca is None or i in paginas_com_marca:
                page.merge_page(watermark_page)

    # Grava o PDF final
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

    print(f"✅ PDF gerado com sucesso: {output_path}")

    #Testar validação de páginas com marcas de água

from manipulator_utils.pdfs import pdfs_paginas

pdfs_paginas = {
    'pdf_exemplo.pdf': [0],
    'pdf_exemplo2.pdf': [0, 1, 2],
    'pdf_exemplo3.pdf': [2, 5] }

from manipulator_utils.manipulator import PDFManipulator

indices_marca_agua = [0, 2, 4]

# Criar o manipulador de PDFs

manipulador = PDFManipulator(
    ficheiro_saida='pdf_final.pdf',
    ficheiro_marca='pdf_watermark.pdf',
    indices_marca_agua=indices_marca_agua
)

# Combinar páginas e aplicar marca de água
manipulador.combinar_pdfs(pdfs_paginas)


#Para estrutura alterada

from manipulator_utils.manipulator import PDFManipulator

# Estrutura de entrada com valores inválidos para testar validação
pdfs_para_compor = {
    'pdf_exemplo.pdf': [0],
    'pdf_exemplo2.pdf': [0, 1, 2],
    'pdf_exemplo3.pdf': [2, 'a', 5, 'Portugal']  
    # itens 'a' e 'Portugal' são inválidos e serão ignorados
}

# Páginas do PDF final onde aplicar a marca de água: 1ª, 3ª e 5ª páginas
indices_marca_agua = [0, 2, 4]

# Criar manipulador e gerar PDF final
manipulador = PDFManipulator(
    ficheiro_saida='pdf_final.pdf',
    ficheiro_marca='pdf_watermark.pdf',
    indices_marca_agua=indices_marca_agua
)
manipulador.combinar_pdfs(pdfs_para_compor)