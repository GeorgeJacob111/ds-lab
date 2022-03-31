from bs4 import BeautifulSoup
import requests

url = "https://www.rottentomatoes.com/top/bestofrt/"
f = requests.get(url)
soup = BeautifulSoup(f.content,'lxml')
#print(soup)

movie = soup.find('table', {'class': 'table'}).find_all('a')
#print(movie)

movie_list = []
num = 0
for anchor in movie:
    urls = "https://www.rottentomatoes.com/"+anchor['href']
    movie_list.append(urls)

#print(movie_list)
num = num+1

murl = urls
f_movie = requests.get(murl)
soup_movie = BeautifulSoup(f_movie.content, 'lxml')

print(soup_movie)

movie_ls = soup_movie.find('div', {'class': 'movie_synopsis clamp clamp-6 js-clamp'})

print(num, urls, '\n'+anchor.string.strip())
#print('Movie Info : '+movie_ls.string.strip())