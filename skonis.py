import bs4 as bs
import urllib.request
import re

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

q = input("search: " )
q = q.replace(' ', '%20').lower()

saucestring2 = 'https://www.skonis-kvapas.lt/index.php?route=product/search&search=' +q

sauce2 = urllib.request.urlopen(saucestring2) #ugly
html2 = sauce2.read()
soup2 = bs.BeautifulSoup(html2, 'lxml')

full_list2 = []
random_dict2 = {}

product_elements2 = soup2.findAll("div", {"class":"product-layout col-xs-12 col-sm-6 col-md-4 col-lg-3"})

for product in product_elements2:
    a2 = product.find("a", href = True)
    link2 = a2['href']

    b2 = product.find('h4')
    product_title2 = b2.get_text()

    c2 = product.find('p', {'class': 'price'})
    product_price2 = c2.text
    product_price2 = product_price2.replace("\n", "")
    product_price2 = product_price2.strip()
    product_price2 = product_price2.replace("", "")
    product_price2 = product_price2.replace("nuo", "")
    product_price2 = product_price2.strip()
    product_price2 = product_price2.replace("€", "")
    len(product_price2)
    if len(product_price2) > 4:
        product_price2 = product_price2[:-4]
    elif len(product_price2)>5:
        product_price2 = product_price2[:-5]
    product_price_2= None
    product_price_2 = float(product_price2)
    print(product_price_2)

    d2 = product.find("div", {"class": "image"})
    imgimg = d2['style']
    product_img1 = re.search('background: #fff url(.*) no-repeat center center;background-size: contain;', imgimg)
    product_img2 = product_img1.group(1)
    product_img2 = product_img2.replace("(", "")
    product_img2 = product_img2.replace(")", "")
    product_img2 = product_img2.replace("'", "")
    print(product_img2)

    random_dict2 = {'img': product_img2, 'price': product_price_2, 'name': product_title2, 'link': link2}
    full_list2.append(random_dict2)
    # full_list2.__len__()

#print(full_list2)

full_slist2 = sorted(full_list2, key = lambda k: k['price'])
print(full_slist2)

