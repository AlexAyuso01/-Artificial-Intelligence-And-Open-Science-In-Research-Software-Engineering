import os
import PyPDF2
import matplotlib.pyplot as plt

# specify folder containing PDF files
folder_path = '/home/alejandro/Documents/UNI/OPTATIVAS/AI-OpenData/PDFs'

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
            axs[1, i].set_title("PDF " + str(i+1))    
            if num_links > 0:
                axs[1, i].hist([num_links], bins=range(0,num_links+2), align='left', color='lightgreen', edgecolor='black')
                

# set common x-axis and title
fig.text(0.5, 0.03, 'Number of Links', ha='center', fontsize=14)
fig.text(0.5, 0.475, 'Number of Figures', ha='center', fontsize=14)
fig.text(0.5, 0.95, 'Distribution of Figures and Links per Article', ha='center', fontsize=14)

# adjust spacing
plt.subplots_adjust(wspace=0.5, hspace=0.425)

# display plot
plt.show()
