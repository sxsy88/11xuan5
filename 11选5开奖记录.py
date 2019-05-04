from lxml import etree
import  requests
import time

with open('11xuan5.csv','w',encoding='utf-8') as f:
    #for a in range(10):
    url = 'https://www.8200.cn/zs_gd11x5/chzs-w-7.htm'
    data = requests.get(url).text
    s = etree.HTML(data)
    file = s.xpath('//*[@id="cpdata"]/tr')
    for div in file:
        times = div.xpath('./td[1]/text()')[0]
        num1 = div.xpath('./td[2]/span/text()')
        num = num1[0] + " " + num1[1]
        f.write('{},{}\n '.format(times,num))






