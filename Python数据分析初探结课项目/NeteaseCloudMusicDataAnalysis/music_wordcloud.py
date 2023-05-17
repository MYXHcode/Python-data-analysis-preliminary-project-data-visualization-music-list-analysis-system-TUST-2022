"""数据可视化，歌单介绍词云图"""
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba
import time


def data_visualization_of_music_wordcloud():
    """歌单介绍词云图"""
    df = pd.read_csv('./music_data/music_detail.csv', header=None)
    text = ''

    print("正在生成歌单介绍词云图片...")

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

    for line in df[2]:
        text += ' '.join(jieba.cut(line, cut_all=False))

    background_image = plt.imread('./music_image/background_image.jpg')

    stopwords = set('')
    stopwords.update(
        ['封面', 'none介绍', '介绍', '歌单', '歌曲', '我们', '自己', '没有', '就是', '可以', '知道', '一起', '不是',
         '因为', '什么', '时候', '还是', '如果', '不要', '那些', '那么', '那个', '所有', '一样', '一直', '不会', '现在',
         '他们', '这样', '最后', '这个', '只是', '有些', '其实', '开始', '曾经', '所以', '不能', '你们', '已经', '后来',
         '一切', '一定', '这些', '一些', '只有', '还有'])

    wc = WordCloud(
        background_color='white',
        mask=background_image,
        font_path='./font_resources/STZHONGS.ttf',
        max_words=2000,
        max_font_size=150,
        random_state=30,
        stopwords=stopwords
    )
    wc.generate_from_text(text)

    # 看看词频高的有哪些,把无用信息去除
    process_word = WordCloud.process_text(wc, text)
    sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
    # print(sort[:50])

    img_colors = ImageColorGenerator(background_image)
    wc.recolor(color_func=img_colors)
    plt.imshow(wc)
    plt.axis('off')

    # 保存图片
    wc.to_file("./music_image/music_wordcloud.png")

    # 显示图片
    plt.show()

    print("\n已生成歌单介绍词云图片，保存至 music_image/music_wordcloud.png")
