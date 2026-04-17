
class PDFManipulator:
    def __init__(self, ficheiro_saida, ficheiro_marca=None, indices_marca_agua=None):
        """
        Inicializa a classe com PDF de saída, marca de água e páginas onde aplicá-la.
        """
        self.ficheiro_saida = ficheiro_saida
        self.ficheiro_marca = ficheiro_marca
        self.indices_marca_agua = indices_marca_agua if indices_marca_agua else []
        self.pagina_pdf_marca_agua = None

        # Carregar marca de água ao inicializar
        if self.ficheiro_marca:
            self._carregar_marca_agua()

    def _carregar_marca_agua(self):
        """
        Lê o PDF da marca de água.
        """
        reader = self.ler_pdf(self.ficheiro_marca)
        if reader:
            self.pagina_pdf_marca_agua = reader.pages[0]
        else:
            print("Marca de água inválida. Nenhuma marca será aplicada.")
            self.pagina_pdf_marca_agua = None

    def ler_pdf(arquivo_pdf):
        """
        Lê um PDF e retorna um PdfReader, tratando erros.
        """
        if not os.path.isfile(arquivo_pdf):
            print(f"Erro: Arquivo '{arquivo_pdf}' não encontrado.")
            return None
        try:
            input_df = PdfReader(arquivo_pdf)
            if len(input_df.pages) == 0:
                print(f"Aviso: O PDF '{arquivo_pdf}' não tem páginas.")
                return None
            return input_df
        except Exception as e:
            print(f"Erro ao ler '{arquivo_pdf}': {e}")
            return None
        
    def validar_indice(indice):
        """
        Valida se o índice é um inteiro não-negativo.
        """
        if not isinstance(indice, int):
            print(f"Aviso: Índice '{indice}' não é um número inteiro e será ignorado.")
            return False
        if indice < 0:
            print(f"Aviso: Índice '{indice}' é negativo e será ignorado.")
            return False
        return True

    def combinar_pdfs(self, pdfs_paginas):
        """
        Combina PDFs e aplica a marca de água nas páginas definidas.
        """
        output_pdf = PdfWriter()
        paginas_finais = []

        for pdf_nome, indices_paginas in pdfs_paginas.items():
            input_df = self.ler_pdf(pdf_nome)
            if input_df is None:
                continue

            total_paginas = len(input_df.pages)
            for indice in indices_paginas:
                if not self.validar_indice(indice):
                    continue
                if indice >= total_paginas:
                    print(f"Aviso: O PDF '{pdf_nome}' não tem a página {indice}.")
                    continue

                pagina_pdf = input_df.pages[indice]

                # Aplica marca de água se esta página estiver na lista
                pagina_final_index = len(paginas_finais)
                if self.pagina_pdf_marca_agua and pagina_final_index in self.indices_marca_agua:
                    pagina_pdf.merge_page(self.pagina_pdf_marca_agua)

                output_pdf.add_page(pagina_pdf)
                paginas_finais.append(pagina_pdf)

        # Salvar PDF final
        try:
            with open(self.ficheiro_saida, "wb") as f_out:
                output_pdf.write(f_out)
            print(f"PDF '{self.ficheiro_saida}' gerado com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar PDF final: {e}")
