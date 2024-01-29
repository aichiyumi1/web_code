'''侧边栏内容拓展练习'''
import streamlit as st

# # 侧边栏基本结构
# page = st.sidebar.radio('我的主页', ['第一页', '第二页', '第三页'])
# if page == '第一页':
#     st.write('这里是第一页')
# elif page == '第二页':
#     st.write('这里是第二页')
# elif page == '第三页':
#     st.write('这里是第三页')

# 练习1-增加其他组件
# page = st.sidebar.radio('我的主页', ['第一页', '第二页', '第三页'])
# with st.sidebar:
#     msg = st.text_input('输入内容')
#     b = st.button('显示内容')
# if page == '第一页':
#     st.write('这里是第一页')
# elif page == '第二页':
#     st.write('这里是第二页')
# elif page == '第三页':
#     st.write('这里是第三页')

# 练习2-增加分组组件
# page = st.sidebar.radio('我的主页', ['第一页', '第二页', '第三页'])
# with st.sidebar:
#     msg = st.text_input('输入内容')
#     b = st.button('显示内容')
#     col1, col2, col3 = st.columns([1, 1, 1])
#     with col1:
#         cb1 = st.checkbox('插入列')
#     with col2:
#         cb2 = st.checkbox('第二列')
#     with col3:
#         cb3 = st.checkbox('第三列')
# if page == '第一页':
#     st.write('这里是第一页')
# elif page == '第二页':
#     st.write('这里是第二页')
# elif page == '第三页':
#     st.write('这里是第三页')

# 练习3-将组件接收的内容显示
page = st.sidebar.radio('我的主页', ['第一页', '第二页', '第三页'])
with st.sidebar:
    msg = st.text_input('输入内容')
    b = st.button('显示内容')
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        cb1 = st.checkbox('插入列')
    with col2:
        cb2 = st.checkbox('第二列')
    with col3:
        cb3 = st.checkbox('第三列')
    if b and msg:
        st.write('将侧边栏的输入内容显示在侧边栏中：', msg)
if page == '第一页':
    st.write('这里是第一页')
elif page == '第二页':
    st.write('这里是第二页')
elif page == '第三页':
    st.write('这里是第三页')
if b and msg:
    st.write('将侧边栏的输入内容显示在主页面中：', msg)
