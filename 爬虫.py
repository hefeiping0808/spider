import requests, re, threading, multiprocess, time, os
from multiprocess.dummy import Pool
from bs4 import BeautifulSoup
from numpy import *
# https://222cce.com/
# https://222cce.com/xiaoshuo/list_120.html
pool = Pool(4)
pool1 = Pool(4)

# 拼接URL
def makeUrl(list):
    list1 = []
    for l in list:
        if 'xingaijiqiao' in l or 'huangsexiaohua' in l:
            pass
        else:
            list1.append('https://222cce.com/htm/' + l)
    return list1
def getStoryUrl(url):
            global txt_list

            list1 = []
            try:
                res = requests.get(url=url, timeout=(10, 15))
                res.encoding = 'utf-8'
                l = re.findall('href="/htm/(.*?)"', res.text, re.S)
                print(l)
                txt_list += l
            except Exception as e:
                # print(e)
                pass
def getText(url):
    global aTime
    try:
        starttime1 = time.time()
        res = requests.get(url=url, timeout=(10, 15))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')
        title = soup.find('h1').text
        text = soup.find('div', class_='content').text
        with open('.\story\\'+title+'.txt', 'w', encoding='utf-8') as f:
            f.write(text)
            nowTime = time.time()-starttime1
            aTime.append(nowTime)
            print(aTime)
            print(title+" 下载完毕！！！", nowTime)
            f.close()
    except Exception as e:
        pass
        # print(e)

if __name__ == '__main__':
    aTime = []
    page_url = []  # 每个翻页内的小说URL
    txt_list = []  # 所有的的小说URL
    starttime = time.time()
    page_url.append('https://222cce.com/xiaoshuo/index.html')
    # for i in range(1, 3):
    #     page_url.append('https://222cce.com/xiaoshuo/list_' + str(i) + '.html')
    pool.map_async(getStoryUrl, page_url)
    pool.close()
    pool.join()
    print('*'*300)
    print(len(makeUrl(txt_list)), makeUrl(txt_list))
    print(f'获取URL用时{time.time()-starttime}')

    pool1.map_async(getText, makeUrl(txt_list))
    pool1.close()
    pool1.join()
    print(f'总用时{time.time()-starttime},平均用时{mean(aTime)}')
