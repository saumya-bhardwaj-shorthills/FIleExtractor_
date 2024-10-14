#!/bin/bash


FILES_DIR="./files"

for file in "$FILES_DIR"/*; do
  if [[ -f "$file" ]]; then
    echo "Processing file: $file"

    python3 main.py "$file"

    if [[ $? -eq 0 ]]; then
      echo "Successfully processed $file"
    else
      echo "Failed to process $file"
    fi

    echo "-------------------------------"
  fi
done
