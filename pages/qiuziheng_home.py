import random
import time
import turtle
import streamlit as st
from PIL import Image


page = st.sidebar.radio('我的首页',['主页','工具分享','图片分享','兴趣分享','词典','留言区','猜单词'])
with st.sidebar:
    msg = st.text_input('输入内容')
    b = st.button('显示内容')
    
def page1():
    st.title('我的首页')
    st.text('''我的网页平平无奇，但诚信希望你有所收获。''')
    st.text('''简介:
                总共有七个页面：
                1.主页：介绍
                2.工具分享：按下不同按键可跳转网页
                3.图片分享：可以将图片进行换色
                4.兴趣分享：将我喜欢的歌曲播放出来
                5.词典：可以查单词有词性，意思和查询次数
                6.留言区
                7.猜单词：会随机获取4个单词每个隔8秒换下一个，然后会询问你这四个单词''')
def page2():
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.write('----')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili','chatgpt','编程猫网页','共创世界'])
    if (go == '我的贴吧'):
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif (go == '我的bilibili') :
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')
    elif (go == 'chatgpt') :
        st.link_button('感谢支持', 'https://chat18.aichatos.xyz/')
    elif (go == '编程猫网页') :
        st.link_button('加油', 'https://shequ.codemao.cn/')
    elif (go == '共创世界') :
        st.link_button('祝你获得许多知识', 'https://www.ccw.site/')

#如何创建跳转按钮
#普通的按钮需要编写if判断触发效果，跳转按钮需要吗？

#应用：兴趣推广_分享链接指引

#注册按键事件处理函数
def page3():
    '我的图片处理工具'

    st.write(':sunglasses:图片换色程序:sunglasses')
    uploaded_file = st.file_uploader('上传图片',type = ['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))
    #获取图片文件的名称、类型和大小
def page4():
    '我的兴趣推荐页'
    st.snow()
    with open('霞光.mp3','rb')as f:
        mypm3 = f.read()
    st.audio(mypm3,format = 'audio/mp3',start_time = 0)
    #with open('玫瑰少年.mp3','rb') as f:
        #mymp3 = f.read()
    #st.audio(mymp3,format = 'audio/mp3',start_time = 0)
        
     
def page5():
    '智慧词典'

    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
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
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    print(words_dict)
    jishu = ['1','3','5','7','9','11','13','15','17','19','21','23','25','27','29']
    oushu = ['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28']
    zhongshu = []
    # 显示查询内容
    if word in words_dict:
        print(words_dict)

        
        # 输出查询的单词内容
        #那咱们就先按空格切割，再按点切割
        if '  ' in words_dict[word][1]:
            cixing=''
            ciyi=''
            cy1=words_dict[word][1].split('  ')#['prep.横越','adv.横穿'] 切成这个样子
            print(cy1)
            for i in cy1:
                cixing += i.split('.')[0] + ' '
                ciyi += i.split('.')[1] + ' '
        else:
            cixing, ciyi = words_dict[word][1].split('.')
            
        st.write('单词的意思是：', ciyi)
        st.text('单词的词性是：' + cixing + '.')
        st.text('这是词典中的第' + str(words_dict[word][0]) + '个单词')        
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.text('单词被查询次数为：' + str(times_dict[n]))
        if word == 'python':
            st.code('''
                        #恭喜你触发彩蛋，这是一行python代码
                        print('hello,word!')''')
        if word == 'snow' or word == 'snowy' or word == 'winter':
            st.snow()

def page6():
    '留言区'

    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8')as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('☀'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🌙'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话：')    
    if st.button('留言'):
        messages_list.append([str((int(messages_list[-1][0]) + 1)), name, new_message])
    message1 = st.text_input('我的回复')
    if st.button('回复'):
        messages_list.append([str((int(messages_list[-1][0]) + 1)), name, message1])

def page7():
    '记单词'

    with open('words_space.txt','r',encoding='utf-8')as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [i[0],i[2]]
    words = []
    for a in range(len(words_list)):
        for v in range(5):
            j = random.sample(words_dict.keys(), 1)
            words.append(j)
        #break
    word.progress(0, '准备开始单词记忆挑战！')
    for i in range(1, 5, 1):
        time.sleep(8)
        word.progress(i*25, words[+i])
    word.progress(4, '开始猜词')
    for p in range(1,5,1):
        w = st.text_input('请输入猜的单词')
        time.sleep(10)
        if w == words[p][1]:
            st.write('答对了')
        elif w == '' :
            st.write('下次请输入')
            time.sleep(10)
            continue
        else:
            st.write('答错了')
            
def img_change(img, rc, gc, bc):
    '图片处理'

    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
        #获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '主页':
    page1()
elif page == '工具分享':
    page2()
elif page == '图片分享' :
    page3()
elif page == '兴趣分享' :
    page4()
elif page == '词典' :
    page5()
elif page == '留言区' :
    page6()
elif page == '猜单词':
    pass
