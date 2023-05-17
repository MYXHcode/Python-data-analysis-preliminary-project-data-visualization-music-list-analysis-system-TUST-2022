"""数据可视化，网易云音乐欧美歌单播放 TOP10"""
import pandas as pd
import matplotlib.pyplot as plt
import time


def data_visualization_of_top_10_ea_song_playlists():
    """网易云音乐欧美歌单播放 TOP10"""
    df = pd.read_csv('./music_data/music_detail.csv', header=None)
    df['play'] = df[4]

    print("正在生成网易云音乐欧美歌单播放 TOP10 图片...")

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

    # 数据排序
    names = df.sort_values(by='play', ascending=False)[0][:10]
    plays = df.sort_values(by='play', ascending=False)['play'][:10]

    # 设置显示数据
    names = [i for i in names]
    names.reverse()
    plays = [i for i in plays]
    plays.reverse()
    data = pd.Series(plays, index=names)

    # 设置图片显示属性,字体及大小
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.unicode_minus'] = False

    # 设置图片显示属性
    plt.figure(figsize=(16, 8), dpi=80)
    ax = plt.subplot(1, 1, 1)
    ax.patch.set_color('white')

    # 设置坐标轴属性
    lines = plt.gca()

    # 设置坐标轴颜色
    lines.spines['right'].set_color('none')
    lines.spines['top'].set_color('none')
    lines.spines['left'].set_color((64/255, 64/255, 64/255))
    lines.spines['bottom'].set_color((64/255, 64/255, 64/255))

    # 设置坐标轴刻度
    lines.xaxis.set_ticks_position('none')
    lines.yaxis.set_ticks_position('none')

    # 绘制柱状图,设置柱状图颜色
    data.plot.barh(ax=ax, width=0.7, alpha=0.7, color=(136/255, 43/255, 48/255))

    # 添加标题,设置字体属性
    ax.set_title('网易云音乐欧美歌单播放 TOP10', fontsize=18, fontweight='light')

    # 添加歌单收藏数量文本
    for x, y in enumerate(data.values):
        num = str(int(y / 10000))
        plt.text(y+1800000, x-0.08, '%s' % (num + '万'), ha='center')

    # 保存图片
    plt.savefig('./music_image/top_10_ea_song_playlists.png', dpi=None)

    # 显示图片
    plt.show()

    print("\n已生成网易云音乐欧美歌单播放 TOP10 图片，保存至 music_image/top_10_ea_song_playlists.png")
