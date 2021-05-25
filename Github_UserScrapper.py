import requests
from bs4 import BeautifulSoup as bs

Github_User = input('Input Github User: ')
url = 'https://github.com/' + Github_User
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img',{'alt':'Avatar'})['src']

print(profile_image)
