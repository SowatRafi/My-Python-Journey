from PyPDF2 import PdfFileReader, PdfFileWriter


def add_encryption(input_pdf, output_pdf, password):
    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    with open(output_pdf, "wb") as file:
        pdf_writer.write(file)


if __name__ == "__main__":
    try:
        add_encryption(
            input_pdf="PDF/Merged PDF/Merged(Paper).pdf",
            output_pdf="PDF/Merged PDF/3D_Tiled_Convolution_for_Effective_Segmentation_of_Volumetric_Medical_Images(locked).pdf",
            password="ASA"
        )

    except Exception as e:
        print(e)
    finally:
        print("End of the program.")
