import streamlit as st
# from 灰度图 import img2char
from PIL import Image

page=st.sidebar.radio("我的首页",["兴趣空间","词典","图片处理","留言区","网址导航"])
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
def page1():
    st.title('欢迎')
    st.text('兴趣不多，拍照为主')
    st.image('chuhaologo.png')
    with open("bgm.mp3","rb") as f:
        mymp3=f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    imgs_name_lst = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg']
    imgs_lst = []
    for i in imgs_name_lst:
        img = Image.open(i)
        imgs_lst.append(img)
    c1, c2, c3= st.columns([1, 1, 1])
    with c1:
        st.image(imgs_lst[0])
        st.write(' ')
    with c2:
        st.image(imgs_lst[1])
        st.write(' ')
    with c3:
        st.image(imgs_lst[2])
        st.write(' ')
    c4,c5,c6,c7=st.columns([1,1,1,1])
    with c4:
        st.image(imgs_lst[3])
        st.write(' ')
    with c5:
        st.image(imgs_lst[4])
        st.write(' ')
    with c6:
        st.image(imgs_lst[5])
        st.write(' ')
    with c7:
        st.image(imgs_lst[6])
        st.write(' ')
def page2():
    '''阿短的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # 显示图片处理界面
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.checkbox('反色滤镜')
            co = st.checkbox('增强对比度')
            bw = st.checkbox('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键"另存为"保存图片')
            st.image(img)

def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img

def page3():
    '''我的词典'''
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    word=st.text_input('输入需查单词')
    if word=='python':
            st.code('''这是一个彩蛋
                    print("Hello World!")
                    Hello World!''')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]#查找编号
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
            if word=='birthday' or word=='balloon' or word=='fun':
                st.balloons()
            elif word=='snow' or word=='winter' or word=='snowy':
                st.snow()    
        with open('check_out_times.txt','w',encoding=='utf-8') as f:
            message=''
            for k,v in times_dict.items():#k编号，v次数:
                message+=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数:',times_dict[n])
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')#读取查询次数，存储在列表中
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        #编号：次数
        times_dict[int(i[0])]=int(i[1])#列表转为字典
            
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
    st.write('----')
    go = st.selectbox('选择想要查看的网页', ['百度', 'bilibili','歌曲宝','几何画板','pyecharts'])
    if go == 'bilibili':
        go1=st.selectbox('你要帮我三连吗', ['必须', '下次一定'])
        if go1=='必须':
            st.link_button('跳转到'+go, 'https://space.bilibili.com/517070645?spm_id_from=333.788.0.0')#问题一
        elif go1=='下次一定':
            st.link_button('跳转到'+go, 'https://www.bilibili.com/')
    elif go == '百度':
        st.link_button('跳转到'+go, 'https://www.baidu.com/')
    elif go == '歌曲宝':
        st.link_button('跳转到'+go, 'https://www.gequbao.com/')
    elif go == '几何画板':
        st.link_button('跳转到'+go,'https://www.desmos.com/geometry/cqc16ha0sj?lang=zh-CN')
    elif go =='pyecharts':
        st.link_button('跳转到'+go,'https://pyecharts.org/#/zh-cn/basic_charts')

if page=="兴趣空间":
    page1()
elif page=="图片处理":
    page2()
elif page=="词典":
    page3()
elif page=="留言区":
    page4()
elif page=="网址导航":
    page5()
    

# python -m streamlit run C:\Users\dell\Desktop\我的网络根据地\zhouchuhao_home.py