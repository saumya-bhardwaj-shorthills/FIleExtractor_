#!/bin/bash

# Directory containing the test files (with subdirectories for PDF, PPTX, DOCX)
TEST_FILES_DIR="./test_files"

# Output directory for storing the extracted data
OUTPUT_DIR="extracted_data_automation"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to process files
process_files() {
    local folder="$1"
    
    # Check if the folder exists and has files
    if [[ -d "$folder" && "$(ls -A "$folder")" ]]; then
        # Loop through all files in the folder
        for file in "$folder"/*; do
            if [[ -f "$file" ]]; then
                echo "Processing file: $file"

                # Run the main.py script with the file path as input
                # This assumes that main.py uses input to get the file path
                python3 main.py <<< "$file"

                # Check if the Python script executed successfully
                if [[ $? -eq 0 ]]; then
                    echo "Successfully processed $file"
                else
                    echo "Failed to process $file"
                fi

                echo "-------------------------------"
            fi
        done
    else
        echo "No files found in $folder"
    fi
}

# Process PDF files
echo "Processing PDF files..."
process_files "$TEST_FILES_DIR/pdf"

# Process PPTX files
echo "Processing PPTX files..."
process_files "$TEST_FILES_DIR/pptx"

# Process DOCX files
echo "Processing DOCX files..."
process_files "$TEST_FILES_DIR/docx"

# Move extracted data to the designated output folder
if [[ -d "extracted_data" ]]; then
    mv extracted_data/* "$OUTPUT_DIR"
    echo "Data moved to $OUTPUT_DIR"
else
    echo "No extracted data found to move."
fi
