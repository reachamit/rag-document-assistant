from pathlib import Path

from pypdf import PdfReader


class PdfService:

    def read_pdfs(self, folder: str):

        documents = []

        pdf_files = Path(folder).glob("*.pdf")

        for pdf in pdf_files:

            reader = PdfReader(pdf)

            for page_number, page in enumerate(reader.pages, start=1):

                text = page.extract_text()

                if text:

                    documents.append(
                        {
                            "file": pdf.name,
                            "page": page_number,
                            "text": text
                        }
                    )

        return documents
    
    def read_pdf(self, file_path: str):

        documents = []

        pdf = Path(file_path)

        reader = PdfReader(pdf)

        for page_number, page in enumerate(reader.pages, start=1):

            text = page.extract_text()

            if text:

                documents.append(
                    {
                        "file": pdf.name,
                        "page": page_number,
                        "text": text
                    }
                )

        return documents