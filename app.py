# -*- coding:UTF-8 -*-

import streamlit as st
from utils import html_temp
from utils import dec_temp
from utils import markdown_text
from eda_app import run_eda_app
from ml_app import run_ml_app
from utils import p_lans

def main():
    # st.markdown(html_temp, unsafe_allow_html=True)

    menu = [
        {"label": "Description"},
        {"label": "EDA"},
        {"label": "Machine Learning"},
        {"label": "About"}
    ]

    choice = st.sidebar.selectbox('Menu', [item['label'] for item in menu])

    # menu = ['Description', 'EDA', 'ML', 'About']
    # choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Description':
        st.markdown("<h1 span style='text-align: center; color: darkblue;'>AMP®-Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Disease Progression Prediction</span><br></br>",
                    unsafe_allow_html=True)
        st.markdown("""
            <style>
                @font-face {
                    font-family: 'JalnanOTF';
                    src: url('./assets/JalnanOTF.otf') format('truetype');
                    font-weight: normal;
                    font-style: normal;
                }
                h3, span {
                    font-family: 'JalnanOTF';
                }
            </style>
        """, unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 24px; color: black;'>🔍 파킨슨병 대회개요</h2>", unsafe_allow_html=True)
        st.markdown("<h3><span style='font-size: 16px; color: black;'>👉 </span><span style='font-size: 16px; color: black;'>파킨슨병 환자의 단백질 및 펩타이드 데이터 측정을 사용하여 질병의 진행을 예측합니다.</span></h3>",
                    unsafe_allow_html=True)
        st.markdown("<h4 style='font-size: 24px; color: black;'>🔬 파킨슨병 연구배경</h2>", unsafe_allow_html=True)
        st.info(markdown_text)

    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'Machine Learning':
        run_ml_app()
    else:
        st.subheader('About')
        # Multiple selection
        lans = ["Python", "HTML", "CSS"]
        myChoice = st.multiselect("💻 사용한 언어", lans, default=["Python", "HTML", "CSS"])


if __name__ == "__main__":
    main()