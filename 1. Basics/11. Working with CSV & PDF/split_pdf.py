from PyPDF2 import PdfFileReader, PdfFileWriter


def split(path_location, name_of_split):
    pdf = PdfFileReader(path_location)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f"{name_of_split}{page}.pdf"
        with open(output, "wb") as output_pdf:
            pdf_writer.write(output_pdf)


if __name__ == "__main__":
    try:
        path = "PDF/1.01.pdf"
        split(path_location=path, name_of_split="PDF/Split PDF/1.01_U-net")

    except Exception as e:
        print(e)
    finally:
        print("End of the program.")
