from PyPDF2 import PdfFileReader, PdfFileWriter


def create_watermark(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # WaterMark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, "wb") as out:
        pdf_writer.write(out)


if __name__ == "__main__":
    try:
        create_watermark(
            input_pdf="PDF/1.01.pdf",
            output="PDF/Watermarked_1.01.pdf",
            watermark="PDF/Watermark-0.pdf"
        )

    except Exception as e:
        print(e)
    finally:
        print("End of the program.")
