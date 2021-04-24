from PyPDF2 import PdfFileReader


def extracted_information(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    text = f"""
    Information about
    {pdf_path}:
    
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(text)
    return information


if __name__ == "__main__":
    path = 'PDF/3D_Tiled_Convolution_for_Effective_Segmentation_of_Volumetric_Medical_Images.pdf'
    extracted_information(path)
