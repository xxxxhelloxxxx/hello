import json

import requests
from bs4 import BeautifulSoup


def ss_scrapy(url):
    request_data = requests.get(url)
    soup = BeautifulSoup(request_data.text, 'lxml')
    ss_data = soup.select('.hover-text > h4')
    ss_dict = {'server': '',
               'server_port': 0,
               'password': '',
               'method': '',
               'remarks': '',
               'auth': False,
               'timeout': 5}
    list_ss = []
    for ss in ss_data:
        s = ss.get_text(strip=True).split(':')
        if s[0] == 'IP Address':
            ss_dict['server'] = s[1]
        elif s[0] == "Port":
            ss_dict['server_port'] = s[1]
        elif s[0] == 'Password':
            ss_dict['password'] = s[1]
        elif s[0] == 'Method':
            ss_dict['method'] = s[1]
            list_ss.append(ss_dict.copy())
    return list_ss


if __name__ == '__main__':
    with open('gui-config.json', 'r+') as f:
        json_data = json.load(f)
        json_data["configs"] = ss_scrapy('https://go.ishadowx.net/')
        f.seek(0)
        json.dump(json_data, f, indent=4)
