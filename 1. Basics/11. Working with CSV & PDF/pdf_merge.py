from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdfs(path_lists, output):
    pdf_writer = PdfFileWriter()

    # Going each path
    for path in path_lists:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, "wb") as out:
        pdf_writer.write(out)


if __name__ == "__main__":
    paths = ["PDF/3D_Tiled_Convolution_for_Effective_Segmentation_of_Volumetric_Medical_Images.pdf",
             "PDF/1.01.pdf",
             "PDF/2.01.pdf",
             "PDF/3.01.pdf",
             "PDF/4.01.pdf",
             "PDF/5.01.pdf",
             "PDF/6.01.pdf",
             "PDF/6.01.pdf",
             "PDF/7.01.pdf",
             "PDF/8.01.pdf",
             "PDF/9.01.pdf",
             "PDF/9.01_Unsupervised.pdf",
             "PDF/10.01.pdf",
             "PDF/11.01.pdf",
             "PDF/12.01.pdf",
             "PDF/13.01.pdf"]
    merge_pdfs(paths, output="PDF/Merged(Paper).pdf")
