import re
from PyPDF2 import PdfReader

def extract_toc(pdf_path):
  try:
    with open(pdf_path, 'rb') as file:
      reader = PdfReader(file)
      toc = reader.outline 
      return toc, reader
  except Exception as e:
    print(f"Error extracting TOC: {e}")
    return None

def print_toc_with_page(toc, reader, level=0):
    for entry in toc:
        if isinstance(entry, list):
            print_toc_with_page(entry, reader, level + 1)
        else:
            title = entry.get('/Title', 'No Title')
            indent = "  " * level
            if re.match(r'^\d+\s', title):
                try:
                    page_num = reader.get_destination_page_number(entry)
                    print(f"{indent}{title} (Page {page_num + 1})")
                except Exception as e:
                    print(f"Error getting page number: {e}")
            else:
                print(f"{indent}{title}")

def print_toc(toc):
    for entry in toc:
        if isinstance(entry, list):
            print_toc(entry)
        else:
            title = entry.get('/Title', 'No Title')
            if re.match(r'^\d+\s', title):
                print(f"{title}")

# Example usage
pdf_file = "inputdoc/Infineon-AURIX_TC3xx_Part1-UserManual-v02_00-EN.pdf" 
toc, reader = extract_toc(pdf_file)

if toc:
    # print_toc(toc)
    print_toc_with_page(toc, reader)

print("Completed!!!! Table of contents extracted and saved to CSV files.")