from pypdf import PdfReader, PdfWriter

def remove_leading_trailing_pages(input_pdf_path, output_pdf_path, leading=1, trailing=1):
    # Load the PDF
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)

    # Calculate valid page range
    start = leading
    end = total_pages - trailing

    if start >= end:
        raise ValueError("The number of pages to remove exceeds the total number of pages.")

    # Create writer and add pages
    writer = PdfWriter()
    for i in range(start, end):
        writer.add_page(reader.pages[i])

    # Save output PDF
    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

    print(f"Saved output PDF without first {leading} and last {trailing} pages to {output_pdf_path}")

# Example usage:
remove_leading_trailing_pages("books/Manifesto.pdf", "books/Manifesto2.pdf", leading=13, trailing=2)

