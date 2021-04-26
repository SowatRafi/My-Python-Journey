#!/usr/bin/env python3
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
            input_pdf=input("Enter your input file path...\n"),
            output_pdf=input("Enter your output file path\n(with new file name)...\nCurrent file name will lock your current PDF.\n"),
            password=input("Enter you password: ")
        )

    except:
        print("\nERROR MESSAGE:")
        print("Nimmddaa…Gojrass thelmii..\nAardha bhos.. Kkraakvikana Bhhumle..\nMohinoojukooo…Lioohakvee…\nUnu Kaasthaa..peezzraaa..\nRoopuveeMinn.. Bahathhee\nZarathraamaa mahashmathee..\nBhreemsaa…Inknoom..Minmahakki..\nChooho..Chuunnamatasweekkdhee..\nThraaa…Ghraakshh…Hooorrr…Aarr..")
    else:
        print("Successfully completed.")
