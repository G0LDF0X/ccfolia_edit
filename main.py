import streamlit as st
from pages import *

# 상태 저장
if "page" not in st.session_state:
    st.session_state["page"] = "HOME"

menus = {"HOME": home, "로그 자르기": edit_text, "이미지 변경하기": image_change,}
with st.sidebar:
    for menu in menus:
        if st.button(menu, use_container_width=True, type = "primary" if st.session_state["page"] == menu else "secondary"):
            st.session_state["page"] = menu
            st.rerun()

st.sidebar.title("CCFOLIA 편집")
st.sidebar.subheader("B 제작")
st.sidebar.text("토이 프로젝트")

st.sidebar.link_button(":computer: GitHub", "https://github.com/G0LDF0X/ccfolia_edit")
st.sidebar.link_button(":fox_face: SNS", "https://twitter.com/Game__B0x")

for menu in menus.keys():
    if st.session_state["page"] == menu:
        menus[menu]()