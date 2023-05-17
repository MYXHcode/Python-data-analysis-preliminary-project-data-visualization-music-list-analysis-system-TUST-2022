"""数据可视化，网易云音乐欧美歌单标签图"""
import squarify
import pandas as pd
import matplotlib.pyplot as plt
import time


def data_visualization_of_label_ea_song():
    """网易云音乐欧美歌单标签图"""
    df = pd.read_csv('./music_data/music_detail.csv', header=None)

    print("正在生成网易云音乐欧美歌单标签图片...")

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

    # 处理标签信息
    tags = []
    dom2 = []

    for i in df[1]:
        c = i.split('-')

        for j in c:
            if j not in tags:
                tags.append(j)
            else:
                continue

    for item in tags:
        num = 0

        for i in df[1]:
            type2 = i.split('-')

            for j in range(len(type2)):
                if type2[j] == item:
                    num += 1
                else:
                    continue

        dom2.append(num)

    # 数据创建
    data = {'tags': tags, 'num': dom2}
    frame = pd.DataFrame(data)
    df1 = frame.sort_values(by='num', ascending=False)
    name = df1['tags'][:10]
    income = df1['num'][:10]

    # 绘图 details
    colors = ['#993333', '#CC9966',  '#333333', '#663366', '#003366', '#009966', '#FF6600', '#FF0033', '#009999',
              '#333366']
    plot = squarify.plot(sizes=income, label=name, color=colors, alpha=1, value=income, edgecolor='white',
                         linewidth=1.5)

    # 设置图片显示属性,字体及大小
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.unicode_minus'] = False

    # 设置标签大小为 1
    plt.rc('font', size=6)

    # 设置标题大小
    plot.set_title('网易云音乐欧美歌单标签图', fontsize=13, fontweight='light')

    # 除坐标轴
    plt.axis('off')

    # 除上边框和右边框刻度
    plt.tick_params(top=False, right=False)

    # 保存图片
    plt.savefig('./music_image/label_ea_song.png', dpi=None)

    # 显示图片
    plt.show()

    print("\n已生成网易云音乐欧美歌单标签图片，保存至 music_image/label_ea_song.png")
