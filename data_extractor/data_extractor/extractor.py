from abc import ABC, abstractmethod
 
class Extractor(ABC):
    def __init__(self, loader):
        self.loader = loader
        self.file = None
        self.file_path = None
    
    def load(self, file_path):
        """Load the file using the appropriate loader based on file type."""
        self.file = self.loader.load_file(file_path)
        self.file_path = file_path
 
    @abstractmethod
    def extract_text(self):
        pass
    
    @abstractmethod
    def extract_images(self):
        pass
    
    # @abstractmethod
    # def extract_urls(self):
    #     pass
    
    @abstractmethod
    def extract_tables(self):
        pass
    
    
    def extract_hyperlinks(document, is_pdf=False):
        """Extract hyperlinks from the document."""
        links = []
        if not is_pdf:
            for rel in document.part.rels.values():
                if "hyperlink" in rel.reltype:
                    links.append({"url": rel.target_ref})
        else:
            for page_num, page in enumerate(document.pages, start=1):
                if '/Annots' in page:
                    annotations = page['/Annots']
                    for annot in annotations:
                        annot_obj = annot.get_object()
                        if '/A' in annot_obj and '/URI' in annot_obj['/A']:
                            links.append({"url": annot_obj['/A']['/URI'], "page_number": page_num})
        return links