import PyPDF2
import os

def merge_pdfs_in_directory(directory_path, output_file):
    pdf_files = [file for file in os.listdir(directory_path) if file.endswith(".pdf")]
    pdf_files = [os.path.join(directory_path, file) for file in pdf_files]
    pdf_files.sort(key=lambda x: os.path.basename(x))

    merger = PyPDF2.PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    with open(output_file, 'wb') as output_pdf:
        merger.write(output_pdf)

    print(f'Merged PDFs from {directory_path} into {output_file}')

# Example usage
if __name__ == "__main__":
    # Directory containing the PDF files to merge
    input_directory = "/path/to/your/pdf/files"
    
    # Output file name
    output_file = input_directory +"/merged.pdf"

    # Merge PDFs in the specified directory
    merge_pdfs_in_directory(input_directory, output_file)