from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter


def rotate_pages(pdf_path, rightORleft):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)

    for i in range(pdf_reader.getNumPages()):
        # Rotate page 90 degrees to the right
        if rightORleft.capitalize() == "Right":
            page = pdf_reader.getPage(i).rotateClockwise(90)
            pdf_writer.addPage(page)
        # Rotate page 90 degrees to the left
        elif rightORleft.capitalize() == "Left":
            page = pdf_reader.getPage(i).rotateCounterClockwise(90)
            pdf_writer.addPage(page)
        else:
            print(f"`{rightORleft}` is not a valid keyword.\nUse (Right) or (Left)")
            break
    """
        # Rotate page 90 degrees to the right
        page_1 = pdf_reader.getPage(0).rotateClockwise(90)
        pdf_writer.addPage(page_1)
        
        # Rotate page 90 degrees to the left
        page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
        pdf_writer.addPage(page_2)
        # Add a page in normal orientation
        pdf_writer.addPage(pdf_reader.getPage(3))
    """
    if rightORleft.lower() == "right" or rightORleft.lower() == "left":
        output_path = f'PDF/90({rightORleft.lower()})rotate_pages.pdf'
        with open(output_path, "wb") as fh:
            pdf_writer.write(fh)

        return output_path

    return "Not created for an `ERROR`"


if __name__ == "__main__":
    path = "PDF/3D_Tiled_Convolution_for_Effective_Segmentation_of_Volumetric_Medical_Images.pdf"
    try:
        rotate = rotate_pages(path, rightORleft=input("Right or Left?\n"))
        print(f"File path : {rotate}")

    except Exception as e:
        print(e)
    finally:
        print("End of the program.")
