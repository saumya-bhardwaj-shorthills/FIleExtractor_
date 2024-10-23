from typing import Any, Dict, List
from data_extractor.data_extractor.extractor import Extractor 
class PPTXExtractor(Extractor):
    def extract_text(self):
        text = ""
        for slide in self.file.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text + "\n"
                if shape.has_table:
                    for row in shape.table.rows:
                        text += "\t".join(cell.text.strip() for cell in row.cells) + "\n"
        return text
 
    def extract_images(self):
        images = []
        for slide_num, slide in enumerate(self.file.slides):
            for shape in slide.shapes:
                if shape.shape_type == 13:  # Picture type
                    images.append({
                        "image_data": shape.image.blob,
                        "ext": shape.image.ext,
                        "page": slide_num + 1,
                    })
        return images
    
    def extract_urls(self):
        #Use the static method from the base class
        return super().extract_hyperlinks(self.file)
    
    def extract_tables(self):
        tables = []
        for slide in self.file.slides:
            for shape in slide.shapes:
                if shape.has_table:
                    tables.append([[cell.text_frame.text.strip() for cell in row.cells] for row in shape.table.rows])
        return tables
has context menu