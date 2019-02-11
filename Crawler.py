#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

dump_num = 2
count = 0
path = './TEMP/'

req = requests.get('http://dcslab.hanyang.ac.kr/?q=node/5')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_cate = soup.select('div > div > div > p > strong')
my_tag = soup.select('div > div > div > ul')

def titles_parser(cate, tag, tar):
    tag = tag[1: len(tag)]
    tar = tar.split('\n')

    for line in tar:
        if not tar:
            continue
        first_index = line.find(', ')
        fir_author = line[0: first_index]

        line = line[first_index: len(line)]
        end_index = line.find('"')
        co_author = line[2: end_index - 2]

        line = line[end_index+1: len(line)]
        end_index = line.find('"')
        title = line[0: end_index]

        line = line[end_index+3: len(line)]
        end_index = line.find(', ')
        name = line[0: end_index]

        line = line[end_index + 2: len(line)]
        location = line

        print(cate)
        print(tag)
        print(fir_author)
        print(co_author)
        print(title)
        print(name)
        print(location)
        write_file(path, cate, tag, fir_author, co_author, title, name, location)
        print('****************************')

def write_file(path, cate, tag, fir, co, title, name, location):
    global count
    title = title.replace('/', )
    ptitle = title.replace(':', '-')
    ptitle = ptitle.replace('/', '-')
    ptitle = ptitle.replace(' ', '-')
    f = open(path + ptitle, 'w', encoding="utf-8")
    data = "---"
    f.write(data)
    data = "\nlayout: publication-single"
    f.write(data)
    data = "\ntitle: " + title
    f.write(data)
    data = '\nname: ' + name
    f.write(data)
    data = '\nfirst-author: ' + fir
    f.write(data)
    data = '\nco-authors: ' + co
    f.write(data)
    data = '\nduring: ' + location
    f.write(data)
    data = '\nlocation: \nimpactfactor: \ndoi: \nnote: '
    f.write(data)
    data = '\ncategories: \n\t- ' + cate
    f.write(data)
    data = '\ntag: \n\t- ' + tag
    f.write(data)
    data = '\n---'
    f.write(data)
    count += 1
    f.close()



def content_parser(strc, cate):
    st = str(strc)
    test = st.split('\n\n')

    for i in range(len(test)):
        tar = test[i]
        if i%2 == 0:
            tag = tar
        else:
            titles_parser(cate, tag, tar)

for i in range(len(my_cate)):
    cate = my_cate[i].text


for i in range(len(my_cate)):
    cate = my_cate[i].text
    content_parser(my_tag[dump_num+i].text, cate)
    print('====================================')
    print(count)




