from urllib.request import urlopen
from bs4 import BeautifulSoup
# to extract the text from the website
def extract_Text_from_website(url):

    url = url
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()    

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

file1 = extract_Text_from_website("https://www.hplovecraft.com/writings/texts/fiction/bws.aspx").lower()
file2 = extract_Text_from_website("https://www.gutenberg.org/files/1342/1342-h/1342-h.htm").lower()

book1 = file1.split()
book2 = file2.split()

#then to get the common words we will use the intersection property

Common_words = set(book1).intersection(book2)
print(Common_words)