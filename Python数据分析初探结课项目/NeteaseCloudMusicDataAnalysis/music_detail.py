"""数据获取，获取歌单详情页的信息"""
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


def get_data_of_music_list_detail_page():
    """获取歌单详情页的信息"""
    df = pd.read_csv('./music_data/music_list.csv', header=None, on_bad_lines=None, names=['url', 'title', 'play',
                                                                                           'user'])

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36 '
    }

    print("正在获取歌单详情页的信息...")

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

    for i in df['url']:
        time.sleep(2)

        url = 'https://music.163.com' + i
        response = requests.get(url=url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # 获取歌单标题
        title = soup.select('h2')[0].get_text().replace(',', '，')

        # 获取标签
        tags = []
        tags_message = soup.select('.u-tag i')

        for p in tags_message:
            tags.append(p.get_text())

        # 对标签进行格式化
        if len(tags) > 1:
            tag = '-'.join(tags)
        else:
            tag = tags[0]

        # 获取歌单介绍
        if soup.select('#album-desc-more'):
            text = soup.select('#album-desc-more')[0].get_text().replace('\n', '').replace(',', '，')
        else:
            text = '无'

        # 获取歌单收藏量
        collection = soup.select('#content-operation i')[1].get_text().replace('(', '').replace(')', '')

        # 歌单播放量
        play = soup.select('.s-fc6')[0].get_text()

        # 歌单内歌曲数
        songs = soup.select('#playlist-track-count')[0].get_text()

        # 歌单评论数
        comments = soup.select('#cnt_comment_count')[0].get_text()

        # 输出歌单详情页信息
        print('\r', title, tag, text, collection, play, songs, comments, end='', flush=True)

        # 将详情页信息写入CSV文件中
        with open('./music_data/music_detail.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(title + ',' + tag + ',' + text + ',' + collection + ',' + play + ',' + songs + ',' + comments +
                    '\n')

        # 获取歌单内歌曲名称
        li = soup.select('.f-hide li a')

        for j in li:
            with open('./music_data/music_name.csv', 'a+', encoding='utf-8-sig') as f:
                f.write(j.get_text() + '\n')

    print("\n已获取歌单详情页的信息，保存至 music_data/music_name.csv")
