#Localização dos pdfs usados:

"C:\Users\ana_m\OneDrive\Desktop\MASTER_D\manipular_pdfs\pdf_exemplo.pdf"
"C:\Users\ana_m\OneDrive\Desktop\MASTER_D\manipular_pdfs\pdf_exemplo2.pdf"
"C:\Users\ana_m\OneDrive\Desktop\MASTER_D\manipular_pdfs\pdf_exemplo3.pdf"
"C:\Users\ana_m\OneDrive\Desktop\MASTER_D\manipular_pdfs\pdf_watermark.pdf"

### Pretende-se que o pdf final seja composto por composto por:

    # página 1 do pdf_exemplo.pdf
    # páginas 1, 2 e 3 do pdf_exemplo2.pdf
    # páginas  2 e 5 do pdf_exemplo3.pdf


pdfs_paginas = {
    'pdf_exemplo.pdf': [0],
    'pdf_exemplo2.pdf': [0, 1, 2],
    'pdf_exemplo3.pdf': [2, 5] }




