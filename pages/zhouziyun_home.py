'''我们的首页'''
import streamlit as st

st.write('CS音乐盒收藏')


page = st.sidebar.radio('音乐盒',['如日中天','人生何处不青山','躺平青年','迈阿密热线','永恒之钻','决心','冲击星'])

with open('{}'.format(page) + '.ogg','rb') as f:#这里rb表示读取二进制文件模式
    mymusic=f.read()#先读取存到变量里
st.audio(mymusic,format='audio/ogg',start_time=0)#再去设置播放哈
