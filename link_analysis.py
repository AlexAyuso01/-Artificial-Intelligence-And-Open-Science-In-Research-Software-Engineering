import os
import PyPDF2
import re
import matplotlib.pyplot as plt4

def link_analysis():
    # specify folder containing PDF files
    # '/home/alejandro/Documents/UNI/OPTATIVAS/AI-OpenData/PDFs'
    folder_path = input('Enter folder path: ')

    # count number of links per article across all files
    links_per_article = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            # open PDF file
            pdf_path = os.path.join(folder_path, file_name)
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                num_links = 0
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text is not None:
                        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
                        num_links += len(urls)
                if num_links > 0:
                    links_per_article.append(num_links)

    # create visualization of number of links per article
    plt4.hist(links_per_article,bins=20)
    plt4.xlabel('Number of Links')
    plt4.ylabel('Frequency')
    plt4.title('Distribution of Links per Article')
    plt4.show()
    plt4.savefig('/home/alejandro/Desktop/IA-OpenData/-Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering/Grobid_out/figure_analysis4.png')
