from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Star_Wars_Episode_III_-_Revenge_of_the_Sith-121766'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
pretty_lxml = soup.encode("utf-8")

print(pretty_lxml)