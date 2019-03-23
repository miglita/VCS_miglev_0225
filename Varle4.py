import bs4 as bs
import urllib.request
import requests
from collections import OrderedDict

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

q = input("search: " )
q = q.replace(' ', '+').lower()

saucestring = 'https://www.assorti.lt/paieska/?query=' +q

# r = requests.get(saucestring, params={'query': q}) #params yra is get, del to nereikia to virsuj (bet vis tik reikia)
# sauce = urllib.request.urlopen(saucestring + q).read() #ugly
sauce = urllib.request.urlopen(saucestring) #ugly
html = sauce.read()
soup = bs.BeautifulSoup(html, 'lxml') #lxml yra parser - daugiau!! #prettier
# print(type(soup))

full_list = []
random_dict = {}

product_elements = soup.findAll("div", {"class":"product_element"})

for product in product_elements:

    a = product.find("a", href = True)
    link = a['href']
    print(link)
    b = product.find("span", {"class": "product_name"})
    product_title = b.text
    c = product.find("span", {"class": "main_price"})
    product_price = c.text
    product_price = product_price.replace(" €", "")
    product_price = product_price.replace(",", ".")
    product_price_= None
    product_price_ = float(product_price)
    d = product.find("img", {"class": "img-responsive center-block product_img"})
    product_img = d['src']
    random_dict = {'img': product_img, 'price': product_price_, 'name': product_title, 'link': link}
    full_list.append(random_dict)
    # full_list.__len__()
print("------------------------")
print(full_list)
#    kwargs_list = full_list(**{random_dict})
#*kwargs ir args

print('-------------------------------------------------------')

full_slist = sorted(full_list, key = lambda k: k['price'])
print(full_slist)

#https://stackoverflow.com/questions/20577840/python-dictionary-sorting-in-descending-order-based-on-values
#kodel neprintina pilno listo ascending


#print sorted(lis, key = lambda i: i['age'])  // https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
