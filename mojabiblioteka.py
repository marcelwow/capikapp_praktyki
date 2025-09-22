import fitz
from typing import List, Dict, Union
import os


class PDFmanager:
    def __init__(self):

        pass

    def fill_form(self, input_path: str, output_path: str, form_data: Dict[str, Union[str, bool]]) -> None:

        try:
            doc = fitz.open(input_path)
            for page in doc:
                fields = page.widgets()
                for field in fields:
                    name = field.field_name
                    if name in form_data:
                        value = form_data[name]
                        if field.field_type == fitz.PDF_WIDGET_TYPE_TEXT:
                            field.field_value = str(value)
                        elif field.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
                            field.field_value = bool(value)
                        elif field.field_type == fitz.PDF_WIDGET_TYPE_RADIOBUTTON:
                            field.field_value = str(value)
                page.update()
            doc.save(output_path)
            doc.close()
        except Exception as e:
            raise Exception(f"Błąd podczas wypełniania. {str(e)}")

    def merge_pdfs(self, pdf_files: List[str], output_path: str) -> None:

        try:
            merged = fitz.open()
            for file in pdf_files:
                if not os.path.exists(file):
                    raise FileNotFoundError(f"Plik nie istnieje: {file}")
                doc = fitz.open(file)
                merged.insert_pdf(doc)
                doc.close()
            merged.save(output_path)
            merged.close()
        except Exception as e:
            raise Exception(f"Błąd podczas łączenia PDFów: {str(e)}")
