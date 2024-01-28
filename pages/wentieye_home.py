'''自己的首页'''
import streamlit as st
import pandas as pd
from PIL import Image
import time



page = st.sidebar.radio('我的首页',['下载','我们的成员','我们的词典','我的留言区','图片处理','新年晚会','坤坤图片','音乐','关于Streamlit'])

PCL_file = "./PCL.exe"


def page1():
    global PCL_file
    with open(PCL_file,"rb") as file:
        btn = st.download_button(
            label="我的世界PCL启动器下载",
            data=file,
            file_name="PCL我的世界启动器.exe",
            mime="application/octet-stream"
        )
    st.text("下载打开后如果出错，请移动到其他文件夹并以管理员权限运行！！！")
    with open('Void.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('001.png')
def page2():
    st.text("籽岷")
    st.text("敬请期待")
def page3():
    '''我的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])#编号：次数
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]#查找编号
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():#k是编号，v是次数
                message += str(k) +  '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word == 'bilibili':
            st.write('恭喜触发了第二个彩蛋')
            st.link_button('跳转到B站', 'https://www.bilibili.com/')
        if word == 'snow' or word == 'snow1':
            st.snow()
def page4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])#st.text(i[1]+':'+i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
def page5():
    st.write(":volcano:图片换色小程序:volcano:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
def page6():
    my_open = st.toggle('开关')
    if my_open:
        st.write('12月31日，看跨年晚会')
        st.write('农历腊月二十九或腊月三十，看春节联欢晚会')
        st.link_button('  跳转到B站    ','https://www.bilibili.com/')
        st.link_button('  跳转到芒果TV  ','https://www.mgtv.com/')
        st.link_button('  跳转到B站直播  ','https://live.bilibili.com/')
        st.write('12月31日、农历腊月二十九或腊月三十记得打开哦！')
        st.balloons()
    else:
        st.write('关闭')
    
def page7():
    st.image('KK1.jpg')
    st.image('KK2.jpg')
    st.image('KK3.jpg')
    st.image('KK4.jpg')
    st.image('KK5.jpg')
def page8():
    st.write('Void')
    with open('Void.mp3','rb') as f:
        mymp3_0 = f.read()
    st.audio(mymp3_0,format='audio/mp3',start_time=0)
    st.write('霞光')
    with open('霞光.mp3','rb') as f:
        mymp3_1 = f.read()
    st.audio(mymp3_1,format='audio/mp3',start_time=0)
    st.write('【FREE】lucky')
    with open('【FREE】lucky.mp3','rb') as f:
        mymp3_2 = f.read()
    st.audio(mymp3_2,format='audio/mp3',start_time=0)
    st.write('Daylight')
    with open('Daylight.mp3','rb') as f:
        mymp3_3 = f.read()
    st.audio(mymp3_3,format='audio/mp3',start_time=0)
    st.write('See You Again')
    with open('See You Again.mp3','rb') as f:
        mymp3_4 = f.read()
    st.audio(mymp3_4,format='audio/mp3',start_time=0)
    st.write('---------------------------------------------')
    st.write('*下载音乐后如为文件，请直接用Windows的音频播放器或QQ音乐播放即可！')
def page9():
    st.write('关于Streamlit：')
    st.write('版本：1.28 SP2 Build 1.28.2')
    st.link_button('Streamlit官网','https://streamlit.io')
    st.write('Copyright 2024 Snowflake Inc. All rights reserved.')

if page == '下载':
    page1()
elif page == '我们的成员':
    page2()
elif page == '我们的词典':
    page3()
elif page == '我的留言区':
    page4()
elif page == '图片处理':
    page5()
elif page == '新年晚会':
    page6()
elif page == '坤坤图片':
    page7()
elif page == '音乐':
    page8()
elif page == '关于Streamlit':
    page9()