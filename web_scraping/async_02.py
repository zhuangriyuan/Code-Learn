import requests
from lxml import etree
from multiprocessing.dummy import Pool
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = "https://www.pearvideo.com/category_5"
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    # print(detail_url, name)

    detail_page_text = requests.get(url=detail_url, headers=headers).text

    countid = detail_url.split("_")[1]
    # print(countid)

    ajax_url = "https://www.pearvideo.com/videoStatus.jsp?"
    params = {
        'contId': countid,
        'mrd': str(random.random())
    }

    ajax_headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400',

        'Referer': 'https://www.pearvideo.com/video_' + countid
    }
    dic_obj = requests.get(url=ajax_url, params=params,
                           headers=ajax_headers).json()
    video_url = dic_obj["videoInfo"]["videos"]["srcUrl"]
    print(video_url)
