import bs4 as bs
import urllib.request
import re
import requests
from collections import OrderedDict

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

q = input("search: " )
q = q.replace(' ', '%20').lower()

saucestring2 = 'https://www.skonis-kvapas.lt/index.php?route=product/search&search=' +q

# r = requests.get(saucestring, params={'query': q}) #params yra is get, del to nereikia to virsuj (bet vis tik reikia)
# sauce = urllib.request.urlopen(saucestring + q).read() #ugly
sauce2 = urllib.request.urlopen(saucestring2) #ugly
html2 = sauce2.read()
soup2 = bs.BeautifulSoup(html2, 'lxml') #lxml yra parser - daugiau!! #prettier
# print(type(soup))

full_list2 = []
random_dict2 = {}

product_elements2 = soup2.findAll("div", {"class":"product-layout col-xs-12 col-sm-6 col-md-4 col-lg-3"})

for product in product_elements2:

    a2 = product.find("a", href = True)
    link2 = a2['href']
    print(link2)
    print('----------------------------------------')
    b2 = product.findAll("h4") #, {"a": "href"}
    product_title2 = b2
    print(product_title2)
    print('-----------------------------------------')
    c2 = product.find("p", {"class": "price"})
    product_price2 = c2.text
    product_price2 = product_price2.replace("nuo", "")
    product_price2 = product_price2.replace("€", "")
    product_price2 = product_price2.replace("\n", "")
    product_price2 = product_price2.strip()
    print(product_price2)
    product_price_2= None
    product_price_2 = float(product_price2)
    print(product_price2)
    #price new // price old
    # print(type(product_price_2))
    print('--------------------------------------------')

    d2 = product.find("div", {"class": "image"})
    imgimg = d2['style']
    product_img1 = re.search('background: #fff url(.*) no-repeat center center;background-size: contain;', imgimg)
    # print(product_img1)
    product_img2 = product_img1.group(1)
    product_img2 = product_img2.replace("(", "")
    product_img2 = product_img2.replace(")", "")
    product_img2 = product_img2.replace("'", "")
    print(product_img2)
    random_dict2 = {'img': product_img2, 'price': product_price_2, 'name': product_title2, 'link': link2}
    full_list2.append(random_dict2)
    # full_list2.__len__()
print("------------------------")
print(full_list2)
#    kwargs_list = full_list(**{random_dict})
#*kwargs ir args

print('-------------------------------------------------------')

full_slist = sorted(full_list, key = lambda k: k['price'])
print(full_slist)

#https://stackoverflow.com/questions/20577840/python-dictionary-sorting-in-descending-order-based-on-values
#kodel neprintina pilno listo ascending


#print sorted(lis, key = lambda i: i['age'])  // https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
