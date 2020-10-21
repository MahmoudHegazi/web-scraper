# You need install :
# pip install PyPDF2 - > Read and parse your content pdf
# pip install requests - > request for get the pdf
# pip install BeautifulSoup - > for parse the html and find all url hrf with ".pdf" final
from PyPDF2 import PdfFileReader
import requests
import io
from bs4 import BeautifulSoup

url=requests.get('https://usda.library.cornell.edu/concern/publications/3t945q76s?locale=en#release-items')
soup = BeautifulSoup(url.content,"lxml")

for a in soup.find_all('a', href=True):
    mystr= a['href']
    if(mystr[-4:]=='.pdf'):
        print ("url with pdf final:", a['href'])
        urlpdf = a['href']
        response = requests.get(urlpdf)
        with io.BytesIO(response.content) as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            txt = f"""
            Author: {information.author}
            Creator: {information.creator}
            Producer: {information.producer}
            Subject: {information.subject}
            Title: {information.title}
            Number of pages: {number_of_pages}
            """
            # Here the metadata of your pdf
            print(txt)
            # numpage for the number page
            numpage=20
            page = pdf.getPage(numpage)
            page_content = page.extractText()
            # print the content in the page 20            
            print(page_content)
