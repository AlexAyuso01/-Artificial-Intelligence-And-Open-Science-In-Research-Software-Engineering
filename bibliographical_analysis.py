import os
from grobid_client.client import GrobidClient

def author_analysis():
    # specify folder containing PDF files
    folder_path = input('Enter folder path: ')


    # create GROBID client
    create_client = GrobidClient()

    # extract author names using GROBID
    author_names = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            # open PDF file
            pdf_path = os.path.join(folder_path, file_name)
            with open(pdf_path, 'rb') as pdf_file:
                grobid_response = create_client.process(pdf_file, output='processHeaderNames')
                if grobid_response:
                    authors = grobid_response['names']['authors']
                    author_names.append([author['name'] for author in authors])
                else:
                    author_names.append([])

    # print author names for each file
    for i, name_list in enumerate(author_names):
        print(f"Authors of file {i}: {', '.join(name_list)}")
