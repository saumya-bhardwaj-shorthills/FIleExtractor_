from typing import Any, Dict, List
from data_extractor.data_extractor.extractor import Extractor
class DOCXExtractor(Extractor):
    def extract_text(self):
        text = ""
        for paragraph in self.file.paragraphs:
            text += paragraph.text + "\n"
        for table in self.file.tables:
            for row in table.rows:
                text += "\t".join(cell.text.strip() for cell in row.cells) + "\n"
        return text
    
    def extract_images(self):
        images = []
        for rel in self.file.part.rels.values():
            if "image" in rel.target_ref:
                images.append({
                    "image_data": rel.target_part.blob,
                    "ext": rel.target_part.content_type.split('/')[1]
                })
        return images
    
    def extract_urls(self):
        # Use the static method from the base class
        return super().extract_hyperlinks(self.file)
    
    def extract_tables(self):
        return [[cell.text.strip() for cell in row.cells] for table in self.file.tables for row in table.rows]