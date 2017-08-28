#to read files- 
#with open('filename') as f:
#    lines = f.readlines()
import requests
from bs4 import BeautifulSoup
import json


def google_sector_report():

    result = {'result':{}}
    with open('Google Finance.htm') as f:
        lines = f.readlines()
        google_finance = ''
        # step 1 读取 Google finance 页面数据
        for line in lines:
            google_finance += line
        google_finance = BeautifulSoup(google_finance, 'lxml')
        # 获得 sector 表格的主 div
        sector_div = google_finance.find('div', {'id':'secperf'})
        # 找到所有 sector 连接, 本题目只取前3个.
        for sector in sector_div.find_all('a')[0:3]:
            # 获取 sector name
            result['result'][sector.get_text()] = {}
            # 获取 sector 变化, 通过取父节点的第二个相邻节点获得.
            result['result'][sector.get_text()]['change'] = \
                float(sector.parent.next_sibling.next_sibling.get_text()
                      .replace('%', '').strip())

        # step2 循环获取每个 sector 数据
        for sector in result['result']:
            # 初始化数据
            sector_page = ''
            result['result'][sector]['biggest_gainer'] = {}
            result['result'][sector]['biggest_loser'] = {}
            with open(sector+'.htm') as f:
                lines = f.readlines()
                for line in lines:
                    sector_page += line
                # 解析某个 secotr 页面
                sector_page = BeautifulSoup(sector_page, 'lxml')
                top_movers = sector_page.find('table', class_='topmovers')
                top_gain = top_movers.find('a')
                # 获取最多升值数据
                result['result'][sector]['biggest_gainer']['equity'] = \
                    top_gain.get_text()
                result['result'][sector]['biggest_gainer']['change'] = \
                    float(top_gain.parent.next_sibling.next_sibling.next_sibling
                          .find_all('span')[1].string
                          .replace('(', '').replace(')', '').replace('%', ''))
                # 获取最多失去数据
                top_loss = top_movers.find('tr',
                                           class_='beginsec').next_sibling.find('a')
                result['result'][sector]['biggest_loser']['equity'] = \
                    top_loss.string
                result['result'][sector]['biggest_loser']['change'] = \
                    float(top_loss.parent.next_sibling.next_sibling.next_sibling
                          .find_all('span')[1].string
                          .replace('(', '').replace(')', '').replace('%', ''))

    # 转化 dict to json
    json_string = json.dumps(result)

    return json_string

print(google_sector_report())
