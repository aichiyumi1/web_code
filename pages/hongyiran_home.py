import urllib.parse
import streamlit as st

page = st.sidebar.radio('我的首页',['音乐搜索','音乐推荐','音乐试听','音乐分享'])

def page4():
    page_1 = st.sidebar.radio('我的主页', ['查看他人分享', '编写分享'])
    st.write('音乐分享区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    if page_1 =='查看他人分享':
        for i in messages_list:
            st.write(i[1],':',i[2])
    elif page_1 =='编写分享':
        name = st.text_input('用户名')
        new_message = st.text_input('写下你分享的音乐名吧~')
        if st.button('留言'):
            if name =='':
                name = '无名氏'
            if new_message =='':
                new_message = '夸赞了作者写的程序'
            messages_list.insert(0,[str(int(messages_list[-1][0])+1), name, new_message])
            #messages_list.append()
            with open('leave_messages.txt', 'w', encoding='utf-8') as f:
                message = ''
                for i in messages_list:
                    message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
                message = message[:-1]
                f.write(message)




def page3():
    sel1 = st.radio('音乐播放：', ['夜曲','爱人错过','奇妙能力歌'])
    if sel1:
        with open(sel1+'.mp3','rb') as f:
            mymp3 = f.read()
        st.audio(mymp3,format='audio/mp3',start_time=0)

def page2():
    st.write('音乐推荐程序')
    sel = st.radio('作者推荐歌手：', ['周杰伦','告五人'],captions=['有许多著名歌曲','有许多经典歌曲'])
    if sel:
        st.link_button('搜索', 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='+urllib.parse.quote(sel))
    sel1 = st.radio('作者推荐音乐：', ['夜曲','爱人错过','奇妙能力歌','精卫','悬拟'],captions=['周杰伦较为经典曲目','经典曲目','不要被普通的名字迷惑了','突然爆火','突然爆火'])
    if sel1:
        st.link_button('搜索', 'https://www.yeyulingfeng.com/tools/music/?name='+urllib.parse.quote(sel1)+'&type=netease') 
    
def page1():
    st.write('音乐搜索程序')
    sel = st.radio('选择网页：', ['音乐搜索器','MyFreeMP3','百乐米','Biu','soundstripe', '铜钟'],
                   captions=['推荐👍\n可以搜索并下载音频', '推荐👍\n可以搜索并下载音频', '有许多国内音乐也有许多国外音乐','有许多国外音乐','有许多国外音乐\n但加载时间较久','搜索需登陆,所以自动改为搜索艺人'])
    sel1 = st.text_input('搜索栏',value='')
    if sel1:
        url = urllib.parse.quote(sel1)
        if sel == '音乐搜索器':
            sel2 = st.radio('选择方式：', ['音乐名称','音乐ID','音乐地址'],
                captions=['输入名称','输入id如 song?id="id" | "id".html | #hash="id" | http:// * / * /"id"', '输入i网址如 http:// * / * '])
            if sel2:
                if sel2 == '音乐名称':
                    st.link_button('搜索名称', 'https://www.yeyulingfeng.com/tools/music/?name='+url+'&type=netease')
                elif sel2 == '音乐ID':
                    st.link_button('搜索ID', 'https://www.yeyulingfeng.com/tools/music/?id='+url+'&type=netease')
                elif sel2 == '音乐地址':
                    st.link_button('搜索地址', 'https://www.yeyulingfeng.com/tools/music/?url='+url)
                    
        elif sel == 'MyFreeMP3':
            st.link_button('搜索名称', 'http://tool.liumingye.cn/music/#/search/M/song/'+url)
        elif sel == '百乐米':
            st.link_button('搜索名称', 'https://bailemi.com/dance/search?type=&key='+url)
        elif sel == 'Biu':
            st.link_button('搜索名称', 'https://biu.moe/#/Song/search?data='+url)
        elif sel == 'soundstripe':
            st.link_button('搜索名称', 'https://app.soundstripe.com/royalty-free-music?filter%5Bq%5D='+url)
        elif sel == '铜钟':
            st.link_button('搜索艺人', 'https://tonzhon.com/artist/'+url)

#python -m streamlit run hongyiran_home.py

if page == '音乐搜索':
    page1()
elif page == '音乐推荐':
    page2()
elif page == '音乐试听':
    page3()
elif page=='音乐分享':
    page4()
else :
    pass
