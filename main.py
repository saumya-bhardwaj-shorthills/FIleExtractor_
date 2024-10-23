import os
from data_extractor.data_extractor.docx_extractor import DOCXExtractor
from data_extractor.data_extractor.pdf_extractor import PDFExtractor
from data_extractor.data_extractor.pptx_extractor import PPTXExtractor
from data_extractor.file_loaders.pdf_loader import PDFLoader
from data_extractor.file_loaders.docx_loader import DOCXLoader
from data_extractor.file_loaders.ppt_loader import PPTLoader
from data_extractor.storage.file_storage import FileStorage
from data_extractor.storage.sql_storage import SQLStorage
from dotenv import load_dotenv
 
load_dotenv()
 
def load_extractor(file_path):
    if file_path.endswith(".pdf"):
        return PDFLoader(), PDFExtractor(PDFLoader())
    elif file_path.endswith(".docx"):
        return DOCXLoader(), DOCXExtractor(DOCXLoader())
    elif file_path.endswith(".pptx") or file_path.endswith(".ppt"):
        return PPTLoader(), PPTXExtractor(PPTLoader())
    else:
        raise ValueError("Unsupported file format. Use PDF, DOCX, or PPTX.")
 
def save_to_storage(file_storage, sql_storage, data, data_type, filename, sql_table_name):
    """Save data to file and SQL storage."""
    if data:
        file_storage.store(data, filename, data_type)
        sql_storage.store(sql_table_name, data)
 
def main():
    # Get configuration from environment variables
    file_path = input("Enter the file path: ")
    database_name = os.getenv("DATABASE_NAME")
    table_names = {
        'text': os.getenv("TABLE_NAME_TEXT"),
        'image': os.getenv("TABLE_NAME_IMAGE"),
        'url': os.getenv("TABLE_NAME_URL"),
        'table': os.getenv("TABLE_NAME_DATA_TABLE")
    }
 
    if not file_path:
        raise ValueError("FILE_PATH is not set in the environment file.")
 
    # Load the appropriate extractor
    loader, extractor = load_extractor(file_path)
    extractor.load(file_path)
 
    # Extract data
    extracted_data = {
        'text': extractor.extract_text(),
        'image': extractor.extract_images(),
        'url': extractor.extract_urls(),
        'table': extractor.extract_tables()
    }
 
    # Create storage directories and initialize FileStorage
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join("extracted_data", base_name)
    file_storage = FileStorage(output_dir)
 
    # Initialize SQLStorage
    sql_storage = SQLStorage(database_name)
 
    # Save extracted data to both file and SQL storage
    for data_type, data in extracted_data.items():
        save_to_storage(file_storage, sql_storage, data, data_type, os.path.basename(file_path), table_names[data_type])
 
    print(f"Extracted data saved to: {output_dir}")
    print("Data stored in SQL database")
    
    sql_storage.close()
 
if __name__ == "__main__":
    main()