from typing import Any, Dict, List
import fitz
from pdf2image import convert_from_path
import pdfplumber
import pytesseract
from data_extractor.data_extractor.extractor import Extractor
class PDFExtractor(Extractor):
    def extract_text(self):
        pages = convert_from_path(self.file_path)
        text = "".join([pytesseract.image_to_string(page, lang='eng') for page in pages])
        return text
 
    def extract_images(self):
        images = []
        pdf_document = fitz.open(self.file_path)
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            for img in page.get_images(full=True):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                images.append({
                    "image_data": base_image["image"],
                    "ext": base_image["ext"],
                    "page": page_num + 1,
                    "dimensions": (base_image["width"], base_image["height"])
                })
        pdf_document.close()
        return images
 
    def extract_urls(self):
        # Use the static method from the base class
        return super().extract_hyperlinks(self.file, is_pdf=True)
    
    def extract_tables(self):
        with pdfplumber.open(self.file_path) as pdf:
            return [table for page in pdf.pages for table in page.extract_tables()]