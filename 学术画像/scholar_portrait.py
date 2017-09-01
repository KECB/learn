import requests
from bs4 import BeautifulSoup
import json
import pandas


def read_file(file_name):
    """
    读取输入内容
    :param file_name:
    :return:
    """
    train_dict = {}
    with open(file_name) as f:
        current_id = ''
        for line in f:
            if '#id' in line.split(':'):
                if current_id != line.split(':')[1]:
                    current_id = line.split(':')[1].strip()
                    train_dict[current_id] = {'name': '', 'org': '',
                                              'search_results_page': '',
                                              'homepage': '', 'pic': '',
                                              'email': '', 'gender': '',
                                              'position': '', 'location': ''}
            if '#name' in line.split(':'):
                train_dict[current_id]['name'] = line.split(':')[1].strip()
            if '#org' in line.split(':'):
                train_dict[current_id]['org'] = line.split(':')[1].strip()
            if '#search_results_page' in line.split(':'):
                train_dict[current_id]['search_results_page'] = line.split(':')[
                    1].strip()

    return train_dict


def scrap_from_google(words, file_name):
    """
    根据给定词语, 缓存 google 第一页搜索结果至指定文件
    https://www.google.com.hk/search?q=[words]
    :param words: 给定的关键词用空格分开
    :param file_name: 要存储的文件名字
    :return
    """
    url = 'https://www.google.com.hk/search?q=' + words
    response = requests.get(url)
    with open(file_name, 'w') as f:
        f.write(response.text)


def analysis_url(url):
    """
    根据连接, 获取其中的数据, 获取指定数据
    :param url:
    :return:
    """
    pass
