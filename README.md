# -Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering
Asignatura de la UPM 

# Text Extraction and Analysis with Grobid

This project demonstrates how to use Grobid and other text analysis tools to extract metadata, bibliographical references, abstracts, figures, and links from a set of open-access articles. The extracted data is then analyzed to generate a keyword cloud, a figure count visualization, and a list of links found in each article.

## Installation

To use this project, you will need to install the following dependencies:

> * Grobid: A machine learning tool for extracting information from scholarly documents. Installation instructions can be found on the Grobid GitHub page.
> * Python 3.7 or later: A programming language used for data analysis and visualization.
> * Python packages: Several Python packages are required for text processing, visualization, and data analysis. These can be installed using the following command:

`pip install -r requirements.txt`

## Usage

To use this project, follow these steps:

> 1. Download the 10 open-access articles in PDF format and store them in a folder on your computer.
> 2. Configure the Grobid installation to point to the location of the PDF files.
> 3. Run the extract_metadata.py script to extract the metadata and bibliographical references from the PDF files.
> 4. Run the extract_abstracts.py script to extract the abstracts from the PDF files.
> 5. Run the extract_figures.py script to extract the figures from the PDF files.
> 6. Run the generate_keyword_cloud.py script to generate a keyword cloud based on the abstracts.
> 7. Run the generate_figure_count_visualization.py script to generate a visualization of the number of figures per article.
> 8. Run the extract_links.py script to extract the links found in each article.

## Sample Output

Examples of the output generated by the text extraction and analysis scripts can be found in the output folder. This includes keyword clouds, figure count visualizations, and links lists.
## Validation Procedures

To ensure the accuracy and quality of the text extraction and analysis results, a combination of automated and manual validation techniques were used. The rationale.md file provides a detailed description of the validation procedures.
## Credits

This project was developed using several third-party tools and libraries, including Grobid, Python, and various Python packages. References and citations used to guide the development of the project are included in the references.md file.