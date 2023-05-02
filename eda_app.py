# -*- coding:UTF-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils
import numpy as np


def run_eda_app():
    # st.markdown("<h1 style='font-size: 24px; color: black;'>EDA (Exploratory Data Analysis)</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h1 span style='text-align: center; color: darkblue;'>EDA </span><span style='text-align: center; color: darkmagenta;'>(Exploratory Data Analysis)</span>",
        unsafe_allow_html=True)
    # "<h1 span style='text-align: center; color: darkblue;'>EDA</span>",
    # unsafe_allow_html = True)

    supplemental = pd.read_csv('data/supplemental_clinical_data.csv')
    st.markdown("<h2 style='font-size: 24px; color: black;'>📋 Supplemental_clinical_data</h2>", unsafe_allow_html=True)
    st.write(supplemental) # print() 라고 생각

    st.markdown("<h3 style='font-size: 24px; color: black;'>🗄️ 데이터 타입</h3>", unsafe_allow_html=True)
    result1 = pd.DataFrame(supplemental.dtypes)
    st.write(result1)

    st.write('<hr>', unsafe_allow_html=True)

    train = pd.read_csv('data/train_clinical_data.csv')
    st.markdown("<h4 style='font-size: 24px; color: black;'>📋 train_clinical_data</h4>", unsafe_allow_html=True)
    st.write(train) # print() 라고 생각

    st.markdown("<h5 style='font-size: 24px; color: black;'>🗄️ 데이터 타입</h5>", unsafe_allow_html=True)
    result2 = pd.DataFrame(train.dtypes)
    st.write(result2)

    st.write('<hr>', unsafe_allow_html=True)

    peptides = pd.read_csv('data/train_peptides.csv')
    st.markdown("<h6 style='font-size: 24px; color: black;'>📋 train_peptides_data</h6>", unsafe_allow_html=True)
    st.write(peptides) # print() 라고 생각

    st.markdown("<h7 style='font-size: 24px; color: black;'>🗄️ 데이터 타입</h7>", unsafe_allow_html=True)
    result3 = pd.DataFrame(peptides.dtypes)
    st.write(result3)

    st.write('<hr>', unsafe_allow_html=True)

    proteins = pd.read_csv('data/train_proteins.csv')
    st.markdown("<h8 style='font-size: 24px; color: black;'>📋 train_proteins_data</h8>", unsafe_allow_html=True)
    st.write(proteins) # print() 라고 생각

    st.markdown("<h9 style='font-size: 24px; color: black;'>🗄️ 데이터 타입</h9>", unsafe_allow_html=True)
    result4 = pd.DataFrame(proteins.dtypes)
    st.write(result4)

    st.write('<hr>', unsafe_allow_html=True)


    # 메뉴 지정
    submenu = st.sidebar.selectbox('Submenu', ['기술통계량', '그래프분석', '통계분석'])
    # if submenu == '기술통계량':
    #     st.dataframe(supplemental)
    #
    #     with st.expander("데이터 타입"):
    #         result1 = pd.DataFrame(supplemental.dtypes)
    #         st.write(result1)
    #     with st.expander("기술 통계량"):
    #         result2 = supplemental.describe()
    #         st.write(result2)
    #     with st.expander("타겟 빈도 수 확인"):
    #         st.write(supplemental['species'].value_counts())
    # elif submenu == '그래프분석':
    #     st.title("Title")
    #     with st.expander("산점도"):
    #         fig = px.scatter(supplemental, x = 'sepal_width',
    #                          y = 'sepal_length',
    #                          color = 'species',
    #                          size = 'petal_width',
    #                          hover_data=['petal_length'])
    #         st.plotly_chart(fig)
    #
    #     # layouts
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         st.title('Seaborn')
    #         # 그래프 작성
    #         fig, ax = plt.subplots()
    #         sns.boxplot(supplemental, x = 'petal_length', y = 'sepal_length', ax=ax)
    #         st.pyplot(fig)
    #
    #     with col2:
    #         st.title('Matplotlib')
    #         # 그래프 작성
    #         fig, ax = plt.subplots()
    #         ax.hist(supplemental['sepal_length'], color='Darkgrey')
    #         st.pyplot(fig)
    #
    #     # Tabs
    #     tab1, tab2, tab3, tab4 = st.tabs(['탭1', '탭2', '탭3', '탭4'])
    #     with tab1:
    #         st.write('탭1')
    #         # 종류 선택할 때마다
    #         # 산점도 그래프가 달라지도록 한다.
    #         # plotly 그래프로 구현
    #         fig = px.scatter(supplemental, x='sepal_width',
    #                          y='sepal_length',
    #                          color='species',
    #                          hover_data=['species'])
    #         st.plotly_chart(fig)
    #
    #     with tab2:
    #         st.write('탭2')
    #         # 캐글 데이터 / 공모전 데이터
    #         # 해당 데이터 그래프 1개만 그려본다.
    #         clinical = pd.read_csv('data/supplemental_clinical_data.csv')
    #         st.write(clinical)
    #
    #         fig, ax = plt.subplots()
    #         ax.hist(clinical['updrs_1'], color='purple')
    #         st.pyplot(fig)
    #
    #     with tab3:
    #         st.write('탭3')
    #
    #     with tab4:
    #         st.write('탭4')
    #
    #
    # elif submenu == '통계분석':
    #     pass
    # else:
    #     st.waring("WARING──!")


