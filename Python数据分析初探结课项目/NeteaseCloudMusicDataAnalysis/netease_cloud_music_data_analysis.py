import os

from music_index import get_data_of_music_list_index_page
from music_detail import get_data_of_music_list_detail_page
from top_10_song import data_visualization_of_top_10_song
from top_10_song_up import data_visualization_of_top_10_song_up
from top_10_ea_song_playlists import data_visualization_of_top_10_ea_song_playlists
from top_10_of_ea_song_collection import data_visualization_of_top_10_of_ea_song_collection
from top_10_of_ea_song_comment import data_visualization_of_top_10_of_ea_song_comment
from top_10_ea_song_collection_distribution import data_visualization_of_top_10_ea_song_collection_distribution
from top_10_ea_song_playlists_distribution import data_visualization_of_top_10_ea_song_playlists_distribution
from label_ea_song import data_visualization_of_label_ea_song
from music_wordcloud import data_visualization_of_music_wordcloud


def menu():
    """网易云音乐数据分析系统菜单"""
    print("欢迎使用网易云音乐数据分析系统！(^▽^ )")
    print("---------------------------------------------")
    print("")
    print("        【网易云音乐数据分析系统】 ")
    print("")
    print("        A.获取歌单索引页的信息")
    print("        B.获取歌单详情页的信息")
    print("        C.生成歌曲出现次数 Top10 图片")
    print("        D.生成歌单贡献 UP 主 TOP10 图片")
    print("        E.生成网易云音乐欧美歌单播放 TOP10 图片")
    print("        F.生成网易云音乐欧美歌单收藏 TOP10 图片")
    print("        G.生成网易云音乐欧美歌单评论 TOP10 图片")
    print("        H.生成欧美歌单收藏数量分布情况图片")
    print("        I.生成欧美歌单播放数量分布情况图片")
    print("        J.生成网易云音乐欧美歌单标签图片")
    print("        K.生成歌单介绍词云图片")
    print("")
    print("---------------------------------------------")
    print("请输入您要进行的操作（输入 quit 退出！）：")


def key_down():
    """网易云音乐数据分析系统功能交互"""
    option = input()

    if option == 'quit' or option == 'QUIT':
        print("已退出！\n\n")
        input()

        exit(0)
    elif option == 'a' or option == 'A':
        # 获取歌单索引页的信息
        get_data_of_music_list_index_page()

        return
    elif option == 'b' or option == 'B':
        # 获取歌单详情页的信息
        get_data_of_music_list_detail_page()

        return
    elif option == 'c' or option == 'C':
        # 生成歌曲出现次数 Top10 图片
        data_visualization_of_top_10_song()

        return
    elif option == 'd' or option == 'D':
        # 生成歌单贡献 UP 主 TOP10 图片
        data_visualization_of_top_10_song_up()

        return
    elif option == 'e' or option == 'E':
        # 生成网易云音乐欧美歌单播放 TOP10 图片
        data_visualization_of_top_10_ea_song_playlists()

        return
    elif option == 'f' or option == 'F':
        # 生成网易云音乐欧美歌单收藏 TOP10 图片
        data_visualization_of_top_10_of_ea_song_collection()

        return
    elif option == 'g' or option == 'G':
        # 生成网易云音乐欧美歌单评论 TOP10 图片
        data_visualization_of_top_10_of_ea_song_comment()

        return
    elif option == 'h' or option == 'H':
        # 生成欧美歌单收藏数量分布情况图片
        data_visualization_of_top_10_ea_song_collection_distribution()

        return
    elif option == 'i' or option == 'I':
        # 生成欧美歌单播放数量分布情况图片
        data_visualization_of_top_10_ea_song_playlists_distribution()

        return
    elif option == 'j' or option == 'J':
        # 生成网易云音乐欧美歌单标签图片
        data_visualization_of_label_ea_song()

        return
    elif option == 'k' or option == 'K':
        # 生成歌单介绍词云图片
        data_visualization_of_music_wordcloud()

        return
    else:
        print("选择错误，请重新输入！\n\n")
        input()

        return


if __name__ == '__main__':
    """运行界面及功能代码"""
    while True:
        menu()
        key_down()

        # 清屏
        os.system('cls')
