# Data Extractor

**Data Extractor** is a Python-based tool designed to extract and store text, images, URLs, and tables from various file formats like PDF, DOCX, and PPTX. The tool supports storing the extracted data locally as files and saving it to a SQL database for future use.

## Features

- **File Format Support**: Extracts data from PDF, DOCX, and PPTX files.
- **Data Extraction**:
  - Text
  - Images
  - URLs (for PDFs and DOCX)
  - Tables (for PDFs and DOCX)
- **Storage**:
  - Save extracted data to local storage.
  - Save extracted data to a SQL database.
- **Modular Architecture**: Easily extendable loaders and extractors for future file formats.
- **Automated Testing**: A bash script to automate the testing of multiple files.

## Project Structure

```bash
.
├── data_extractor/
│   ├── data_extractor/
│   │   ├── docx_extractor.py
│   │   ├── pdf_extractor.py
│   │   └── pptx_extractor.py
│   ├── file_loaders/
│   │   ├── docx_loader.py
│   │   ├── pdf_loader.py
│   │   └── ppt_loader.py
│   ├── storage/
│   │   ├── file_storage.py
│   │   └── sql_storage.py
├── extracted_data/
├── files/           # Input files for extraction
├── main.py          # Main script
├── test_files.sh    # Bash script for automating tests
├── README.md
└── requirements.txt
```

## Prerequisites

To run this project, you'll need:

- Python 3.x
- Required Python libraries, which are listed in the `requirements.txt` file.

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Running the `main.py`

You can run the `main.py` script manually by passing a file path as an argument:

```bash
python3 main.py <path_to_file>
```

Example:

```bash
python3 main.py ./files/sample.pdf
```

### 2. Automating Tests for Multiple Files

You can test multiple files stored in the `files` folder using the provided bash script `test_files.sh`.

#### Steps:

1. Ensure the script has executable permissions:

```bash
chmod +x test_files.sh
```

2. Run the script:

```bash
./test_files.sh
```

This will automatically process each file in the `files` directory and extract its contents.

### 3. Storing Data

- **Local Storage**: Extracted data (text, images, URLs, tables) will be stored in the `extracted_data` directory.
- **SQL Storage**: Extracted data will also be stored in a SQL database. You can configure the database connection in the `SQLStorage` class.

## How It Works

1. **File Loaders**: The tool identifies the type of file (PDF, DOCX, or PPTX) and loads it using the appropriate loader (`PDFLoader`, `DOCXLoader`, `PPTLoader`).
   
2. **Data Extraction**: The file is processed by a corresponding extractor (`PDFExtractor`, `DOCXExtractor`, `PPTXExtractor`) that extracts text, images, URLs, and tables.

3. **Storage**: 
   - The extracted data is saved to a local folder (`extracted_data`).
   - The extracted data is also stored in a SQL database using `SQLStorage`.

## File Storage

Extracted data is saved in the following format under the `extracted_data` folder:

- Text: `text/`
- Images: `image/`
- URLs: `url/`
- Tables: `table/`

The files are stored under directories named after the base name of the input file.

Example for `sample.pptx`:

```
extracted_data/
└── sample/
    ├── text.txt
    ├── image1.png
    ├── image2.png
    ├── urls.txt
    └── table1.csv
```

## SQL Database

The extracted data can be stored in a SQL database using the `SQLStorage` class. The tables used are:

- `text`
- `image`
- `url`
- `data_table`

