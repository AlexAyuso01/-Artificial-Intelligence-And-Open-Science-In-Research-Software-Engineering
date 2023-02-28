import os
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import PyPDF2

folder_path = '/home/alejandro/Documents/UNI/OPTATIVAS/AI-OpenData/PDFs'

def abstract_analysis():
    # function to extract abstract text from a PDF file using Grobid
    def extract_abstract(file_path):
        url = 'http://localhost:8070/api/processHeaderDocument'
        params = {'input': open(file_path, 'rb')}
        response = requests.post(url, files=params)
        soup = BeautifulSoup(response.text, 'lxml')
        abstract = soup.find('abstract').text
        return abstract

    # get file paths for all PDFs in a folder

    pdf_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # extract abstracts and preprocess text
    abstracts = []
    for pdf_path in pdf_paths:
        abstract = extract_abstract(pdf_path)
        tokens = nltk.word_tokenize(abstract)
        tokens = [token.lower() for token in tokens if token.isalpha()]
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]
        abstracts.append(' '.join(tokens))

    # generate word clouds and plot in grid
    num_rows = 2
    num_cols = 5
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 8))
    for i, abstract in enumerate(abstracts):
        row = i // num_cols
        col = i % num_cols
        wordcloud = WordCloud(width=400, height=400, background_color='white').generate(abstract)
        axs[row, col].imshow(wordcloud, interpolation='bilinear')
        axs[row, col].set_title(f'Paper {i+1}')
        axs[row, col].axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    plt.savefig('/home/alejandro/Desktop/IA-OpenData/-Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering/Grobid_out/figure_analysis.png')

def figures_and_links_analysis():
    # initialize figure
    fig, axs = plt.subplots(nrows=2, ncols=len(os.listdir(folder_path)), figsize=(16,8))

    # count number of figures and links per article across all files
    for i, file_name in enumerate(os.listdir(folder_path)):
        if file_name.endswith('.pdf'):
            # open PDF file
            pdf_path = os.path.join(folder_path, file_name)
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                num_figures = 0
                num_links = 0
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if 'Figure' in text:
                        num_figures += 1
                    if 'http' in text:
                        num_links += text.count('http')
                axs[0, i].set_title("PDF " + str(i+1))
                if num_figures > 0:
                    axs[0, i].hist([num_figures], bins=range(0,num_figures+2), align='left', color='lightblue', edgecolor='black')
                else:  
                    axs[0, i].text(0.5, 0.5, 'None', horizontalalignment='center', verticalalignment='center', color='red')

                axs[1, i].set_title("PDF " + str(i+1))    
                if num_links > 0:
                    axs[1, i].hist([num_links], bins=range(0,num_links+2), align='left', color='lightgreen', edgecolor='black')
                else:  
                    axs[1, i].text(0.5, 0.5, 'None', horizontalalignment='center', verticalalignment='center', color='red')
                    

    # set common x-axis and title
    fig.text(0.5, 0.03, 'Number of Links', ha='center', fontsize=14)
    fig.text(0.5, 0.475, 'Number of Figures', ha='center', fontsize=14)
    fig.text(0.5, 0.95, 'Distribution of Figures and Links per Article', ha='center', fontsize=14)

    # adjust spacing
    plt.subplots_adjust(wspace=0.5, hspace=0.425)

    # display plot
    plt.show()

    #store the figures in the folder Grobid_out 
    plt.savefig('/home/alejandro/Desktop/IA-OpenData/-Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering/Grobid_out/figure_analysis2.png')
