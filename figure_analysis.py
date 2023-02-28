import os
import PyPDF2
import matplotlib.pyplot as plt3


#create the function figure_analysis2 
def figure_analysis():
    # specify folder containing PDF files
    folder_path = '/home/alejandro/Documents/UNI/OPTATIVAS/AI-OpenData/PDFs'

    # count number of figures per article across all files
    figures_per_article = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            # open PDF file
            pdf_path = os.path.join(folder_path, file_name)
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                num_figures = 0
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if 'Figure' in text:
                        num_figures += 1
                    elif num_figures > 0:
                        figures_per_article.append(num_figures)
                        num_figures = 0
                if num_figures > 0:
                    figures_per_article.append(num_figures)

    # create visualization of number of figures per article
    plt3.hist(figures_per_article)
    plt3.xlabel('Number of Figures')
    plt3.ylabel('Frequency')
    plt3.title('Distribution of Figures per Article')
    plt3.show()
    plt3.savefig('/home/alejandro/Desktop/IA-OpenData/-Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering/Grobid_out/figure_analysis3.png')
