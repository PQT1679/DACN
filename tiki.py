import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

URL = "https://tiki.vn/sach-ky-nang-song/c870"

page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content.decode(), "html.parser")
container =soup.find(class_='ProductList__Wrapper-sc-1dl80l2-0 Kxajl')
products = container.find_all(class_='product-item',limit=7)
host = 'https://tiki.vn'
for p in products:
    url =host+p['href']
    pagedetails = requests.get(url,headers=headers)
    soup = BeautifulSoup(pagedetails.content, "html.parser")
    book = soup.find(class_='styles__StyledProductContent-sc-1f8f774-0 ewqXRk')
    title=book.find(class_='title').string
    price=0
    sold =book.find(class_='styles__StyledQuantitySold-sc-1u1gph7-2 exWbxD').string
    print("Tên Sách: "+title)
    try:
        price=book.find(class_='product-price').find_all('div')[0].string
    except:
        price=book.find(class_='flash-sale-price').span.string
    print("Giá: "+price)
    try:
        author =book.find(class_='brand-and-author').h6.a.string
        if not author ==None:
            print("Tác giả: "+author)
    except:
        pass
    print(sold)
    try:
        content=soup.find(class_='content has-table')
        rows =content.find_all('tr')
        for row in rows:
            td = row.find_all('td')
            print(td[0].string+' : '+td[1].string)
    except:
        pass
    print('--------------------')
    