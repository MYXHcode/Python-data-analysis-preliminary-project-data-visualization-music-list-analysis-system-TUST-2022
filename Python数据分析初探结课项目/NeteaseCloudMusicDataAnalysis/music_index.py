"""数据获取，获取歌单索引页的信息"""
from bs4 import BeautifulSoup
import requests
import time


def get_data_of_music_list_index_page():
    """获取歌单索引页的信息"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36 '
    }

    print("正在获取歌单索引页的信息...")

    # 输出进度条
    t = 60
    start = time.perf_counter()

    for i in range(t + 1):
        finsh = "▓" * i
        need_do = "-" * (t - i)
        progress = (i / t) * 100
        dur = time.perf_counter() - start

        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")

        time.sleep(0.02)

    for i in range(0, 1330, 35):
        # print('\r', i, end='', flush=True)

        time.sleep(2)

        url = 'https://music.163.com/discover/playlist/?cat=欧美&order=hot&limit=35&offset=' + str(i)
        response = requests.get(url=url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # 获取包含歌单详情页网址的标签
        ids = soup.select('.dec a')

        # 获取包含歌单索引页信息的标签
        lis = soup.select('#m-pl-container li')
        # print('\r', len(lis), end='', flush=True)

        for j in range(len(lis)):
            # 获取歌单详情页地址
            url = ids[j]['href']

            # 获取歌单标题,替换英文分割符
            title = ids[j]['title'].replace(',', '，')

            # 获取歌单播放量
            play = lis[j].select('.nb')[0].get_text()

            # 获取歌单贡献者名字
            user = lis[j].select('p')[1].select('a')[0].get_text()

            # 输出歌单索引页信息
            print('\r', url, title, play, user, end='', flush=True)

            # 将索引页写入CSV文件中
            with open('./music_data/music_list.csv', 'a+', encoding='utf-8-sig') as f:
                f.write(url + ',' + title + ',' + play + ',' + user + '\n')

    print("\n已获取歌单索引页的信息，保存至 music_data/music_list.csv")
