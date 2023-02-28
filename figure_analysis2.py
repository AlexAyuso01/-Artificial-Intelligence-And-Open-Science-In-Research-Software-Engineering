import os
import PyPDF2
import matplotlib.pyplot as plt

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
plt.hist(figures_per_article)
plt.xlabel('Number of Figures')
plt.ylabel('Frequency')
plt.title('Distribution of Figures per Article')
plt.show()
