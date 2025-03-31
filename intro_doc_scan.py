# This code extracts text from a PDF
# and adds the extracted text to a list

# import library
import PyPDF2

# extact text
def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []
        
        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
        
        return pdf_text

# run command
if __name__ == "__main__": 
  extract_text = extract_text_from_pdf('req30848.pdf') 
  for text in extract_text:
    print(text)
