import requests
from bs4 import BeautifulSoup
URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
container = soup.find(class_='lister-list')
movies= container.find_all('tr',limit=5)
for movie in movies:
    titlecolumn = movie.find(class_="titleColumn")
    moviename ='Tên Phim: '+ titlecolumn.a.string
    actvsdir =titlecolumn.a['title'].split(' (dir.), ')
    actors = 'Diễn Viên Chính: '+actvsdir[1]
    directors= 'Đạo Diễn: '+actvsdir[0]
    year = movie.find(class_='secondaryInfo').string
    year = year.replace('(','').replace(')','')
    year = 'Năm ra mắt: '+year 
    rating = movie.select("td.ratingColumn.imdbRating")[0].strong.string
    rating = 'Điểm đánh giá: '+rating
    print(moviename)
    print(directors)
    print(actors)
    print(year)
    print(rating)
    print('---------------')