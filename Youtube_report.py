#!/usr/lib/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from selenium import webdriver
import datetime
import time
from slacker import Slacker

options=webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)
driver.get('https://www.youtube.com/feed/trending?gl=KR')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

title=[]
channel=[]
view=[]
datetime=[]
description=[]
for source in soup.find_all('ytd-video-renderer',class_='style-scope ytd-expanded-shelf-contents-renderer', limit=10) :
    title.append(source.find_all('a',{'id':'video-title'})[0].string)
    channel.append(source.find_all('a',class_='yt-simple-endpoint style-scope yt-formatted-string')[0].string)
    view.append(source.find_all('span',class_='style-scope ytd-video-meta-block')[0].string)
    datetime.append(source.find_all('span',class_='style-scope ytd-video-meta-block')[1].string)
    description.append(source.find_all('yt-formatted-string',{'id':'description-text'})[0].string)
driver.close()

youtube_output = []
for i in range(10) :
    youtube_output.append(str(i+1)+". ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ \n"+str(title[i].strip())+" \n"+str(channel[i])+" | "+str(view[i])+" | "+str(datetime[i])+" \n\n"+str(description[i])+" \n\n")

token = 'your_token'
slack = Slacker(token)
attachments_dict = dict()
attachments_dict['pretext'] = " 현시점 유튜브 인기급상승 동영상 10 "
attachments_dict['title'] = "유튜브에서 확인하기"
attachments_dict['title_link'] = "https://www.youtube.com/feed/trending?gl=KR"
attachments_dict['fallback'] = ""
attachments_dict['text'] = "".join(youtube_output)
attachments = [attachments_dict]
slack.chat.post_message(channel="#your_chennel", text=None, attachments=attachments)
