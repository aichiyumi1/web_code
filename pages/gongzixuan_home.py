import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['自我介绍', '兴趣推荐', '图片处理', '智慧词典', '留言区', '音乐', '网址导航'])

def page1():
    st.write('欢迎来到我的网络根据地。')
    st.write('本人是动漫爱好者。')
    st.write('尤其喜欢看《名侦探柯南》以及《魔术快斗1412》。')
    st.write('有兴趣的可以去看看！具体介绍见‘兴趣推荐’。')
    st.write('🥰')
    st.write('🥳')
    st.write('除此之外，本人琴、棋、书、画样样精通，还喜欢编程、打乒乓球和宅在家里看书。')
    st.write('尤其擅长编程和乒乓球。')
    st.write('好了，废话不多说，赶快去看看我的网络根据地吧！')
    st.write('🥰')
    st.write('🥳')

def page2():
    '兴趣推荐'
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('英文.png')
    st.write('----------------------------')
    st.write('动漫')
    st.write('1.《名侦探柯南》')
    st.image('柯南.jpg')
    st.image('柯哀CP1.jpg')
    st.write('                              ')
    st.write('2.《魔术快斗1412》or《魔术快斗》')
    st.image('快红CP5.png')
    st.image('快红CP2.png')
    st.write('                              ')
    st.write('小说')
    st.write('1.《哈利·波特》系列')
    st.image('哈利波特.jpg')
    st.write('2.《绿野仙踪》')
    st.image('绿野仙踪.jpg')
    
def page3():
    '''我的图片处理工具'''
    st.write(":rainbow:图片换色小程序:rainbow:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))
        
def page4():
    '''智慧词典'''
    st.image('词典.jpg')
    st.write('📖智慧词典📖')
    # 从本地文件中将词典信息读取出来， 并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容在进行分割，分为“编号、单词、解释”
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
    word  = st.text_input('请输入要查询的单词')
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
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        # 注意词典中没有python，需要自行添加数据
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word == 'snow':
            st.snow()
        if word == 'balloon':
            st.balloons()
        if word == 'banquet':
            st.balloons()
        if word == 'Strange thieves':
            st.write('恭喜你触发彩蛋，这是一段音频。')
            with open('英语彩蛋.m4a', 'rb') as f:
                mymp3 = f.read()
            st.audio(mymp3, format='audio/mp3', start_time=0)
            
def page5():
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
        elif i[1] == '怪盗基德':
            with st.chat_message('🍀'):
                st.write(i[1],':',i[2])#st.text(i[1]+':'+i[2])
        elif i[1] == '江户川柯南':
            with st.chat_message('👓'):
                st.write(i[1],':',i[2])#st.text(i[1]+':'+i[2])
        elif i[1] == '灰原哀':
            with st.chat_message('💊'):
                st.write(i[1],':',i[2])#st.text(i[1]+':'+i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫', '怪盗基德', '江户川柯南', '灰原哀'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
        
def page6():
    '''音乐'''
    st.write('霞光')
    st.image('霞光.jpg')
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('如果有你在')
    st.image('如果有你在.jpg')
    with open('如果有你在.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('世纪末的魔术师')
    st.image('世纪末的魔术师.jpg')
    with open('世纪末的魔术师.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)

def page7():
    '''网址导航'''
    st.write('网址导航')
    st.write('百度：https://www.baidu.com/')
    st.image('百度1.png')
    st.write('百度贴吧：https://tieba.baidu.com/')
    st.image('百度贴吧.png')
    st.write('编程猫社区：https://shequ.codemao.cn/')
    st.image('编程猫社区.png')
    st.write('腾讯视频：https://v.qq.com/')
    st.image('腾讯视频.png')
    st.write('哔哩哔哩：https://www.bilibili.com/')
    st.image('哔哩哔哩.jpg')
    st.write('抖音：https://www.douyin.com/')
    st.image('抖音.png')
    st.write('心怀宇宙天地宽：https://blog.sciencenet.cn/home.php?mod=space&uid=3061&do=blog&view=me&from=space')
    st.image('心怀宇宙天地宽.png')
    st.write('坯逆翘楚的盗闲居：https://wgwxws.site/')
    st.image('坯逆翘楚的盗闲居.png')
    st.write('程序员无所不能：https://wiltchamberian.github.io/')
    st.image('程序员无所不能.png')
    st.write('荒原之梦：https://zhaokaifeng.com/category/extraordinary-edition/science-and-technology-encyclopedia/')
    st.image('荒原之梦.png')

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
            img_array[x, y] = (g, r, b)
    return img

if page=='自我介绍':
    page1()
elif page=='兴趣推荐':
    page2()
elif page=='图片处理':
    page3()
elif page=='智慧词典':
    page4()
elif page=='留言区':
    page5()
elif page=='音乐':
    page6()
elif page=='网址导航':
    page7()

