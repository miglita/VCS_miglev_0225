import bs4 as bs
import urllib.request
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

q = input("search: " )
q = q.replace(' ', '+').lower()


#saucestring = 'https://www.assorti.lt/paieska/?' + q #query='
saucestring = 'https://www.assorti.lt/paieska/?query=' +q

# r = requests.get(saucestring, params={'query': q}) #params yra is get, del to nereikia to virsuj (bet vis tik reikia)
#print(saucestring)
# sauce = urllib.request.urlopen(saucestring + q).read() #ugly
sauce = urllib.request.urlopen(saucestring) #ugly
html = sauce.read()
soup = bs.BeautifulSoup(html, 'lxml') #lxml yra parser - daugiau!! #prettier
# print(type(soup))

#------------------------------------------------------------
# rezai - padaryti page 1, page 2. sitas bent veikia
# for url in soup.find_all('a'): #class_ = explain please; finds all of the text between div tags
#     print(url) #tas class_ tiesiog kintamasis? // , class_='grid-item product  first'
#------------------------------------------------------------
#div_containers = soup.findAll("div", {"class":"product_element"})

full_list = []
random_dict = {}

for product_search in soup.findAll("div", {"class": "product_listing search"}):
    product_list = product_search
    print(product_list)

    for product_list in soup.findAll("div", {"class":"product_element"}):
        product_content_clearfix = product_list
        print(product_content_clearfix)
            for product_element in soup.findAll("div", {"class":"content clearfix"}):
                product = product_element.div
                print(product)


# for product_search in soup.findAll("div", {"class": "product_listing search"}):
#     product_list = product_search
#     print(product_list)
#
#     for product_list in product_search.findAll("div", {"class":"product_element"}):
#         product_content_clearfix = product_list
#         print(product_content_clearfix)
# for product_element in product_list.findAll("div", {"class":"product_element"}):
#     product = product_element
#     print(product)

full_list = []
random_dict = {}

product_elements = soup.findAll("div", {"class":"product_element"})

for product in product_elements:
    print("--------")
    # print(product)
    # print(product)
    a = product.find("a", href = True)
    link = a['href']
    print(link)
    b = product.find("span", {"class": "product_name"})
    product_title = b.text
    c = product.find("span", {"class": "main_price"})
    product_price = c.text
    d = product.find("img", {"class": "img-responsive center-block product_img"})
    product_img = d['src']

    random_dict = {'img': product_img, 'price': product_price, 'name': product_title, 'link': link}
    full_list.append(random_dict)
    full_list.__len__()




# for product_element in product_lising:
#     img = product_element.find(img)
#     price = product_element.find(span class price)
#     name = product_element.find(span name)
#     link = product_element.find(a href)
#     random_dict = {'img': img, 'price': price, 'name': name, 'link': link}
#     full_list.append(random_dict)
# for img in soup.findAll("img", {"class": "img-responsive center-block product_img"}):
#     product_img_src = img['src']
#     #print(product_img_src)
#
# product
#
#     img = product_element.find(img)
#     price = product_element.find(span class price)
#     name = product_element.find(span name)
#     link = product_element.find(a href)
#     random_dict = {'img': img, 'price': price, 'name': name, 'link': link}
#     full_list.append(random_dict)
#
# for product in full_list:
#     product['name']
# #-----------------------------------------------------------------------------
# produktas = {}
# for div_container in div_containers: # tada sito rasyti is naujo nereikia ->('div', {'class':'product_element'})
#     product_link = div_container.a['href']
#     #print(product_link)
#
# for span_container in soup.findAll("span", {"class": "product_name"}):
#     product_title = span_container.text
#     #print(product_title)
#
# for span_container_price in soup.findAll("span", {"class": "main_price"}):
#     product_price = span_container_price.text
#     #print(product_price)
#
# for img in soup.findAll("img", {"class": "img-responsive center-block product_img"}):
#     product_img_src = img['src']
#     #print(product_img_src)
#
# print("nuoroda: " + product_link)
# print("pavadinimas: " + product_title)
# print("kaina: " + product_price)
# print("paveiksliukas: " + product_img_src)
# #-----------------dictionaris liste--------------------------
# full_list = []
# random_dict = {}
#
# for product_element in product_lising:
#     img = product_element.find(img)
#     price = product_element.find(span class price)
#     name = product_element.find(span name)
#     link = product_element.find(a href)
#     random_dict = {'img': img, 'price': price, 'name': name, 'link': link}
#     full_list.append(random_dict)
#
# for product in full_list:
#     product['name']
#
#
# #---------------------------------------------------------------------------
#
# soup=...(page_html, "html.parser")
# containers=page_soup.findAll("div", {"class":"item-container"})
# # for container in containers:
# #     product_link = container.div.a['']
#
# # title_container = container.findAll("a", {"class":"item-title"})
# # product_name = title_container[0].text
# #
# # shipping_container=container.findAll("li", {"class":"price-ship"})
# # shipping=shipping_container[0].text.strip()
# #
# # print("brand: " + brand)
# # print("product_name: " + product_name)
# print("shipping: " + shipping)