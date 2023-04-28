# -*- coding:UTF-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils
import numpy as np


def run_eda_app():
    st.subheader("탐색적 자료 분석")

    iris = pd.read_csv('data/iris.csv')
    st.markdown('## IRIS 데이터 확인')
    st.write(iris) # print() 라고 생각


    # 메뉴 지정
    submenu = st.sidebar.selectbox('Submenu', ['기술통계량', '그래프분석', '통계분석'])
    if submenu == '기술통계량':
        st.dataframe(iris)

        with st.expander("데이터 타입"):
            result1 = pd.DataFrame(iris.dtypes)
            st.write(result1)
        with st.expander("기술 통계량"):
            result2 = iris.describe()
            st.write(result2)
        with st.expander("타겟 빈도 수 확인"):
            st.write(iris['species'].value_counts())
    elif submenu == '그래프분석':
        st.title("Title")
        with st.expander("산점도"):
            fig = px.scatter(iris, x = 'sepal_width',
                             y = 'sepal_length',
                             color = 'species',
                             size = 'petal_width',
                             hover_data=['petal_length'])
            st.plotly_chart(fig)

        # layouts
        col1, col2 = st.columns(2)
        with col1:
            st.title('Seaborn')
            # 그래프 작성
            fig, ax = plt.subplots()
            sns.boxplot(iris, x = 'petal_length', y = 'sepal_length', ax=ax)
            st.pyplot(fig)

        with col2:
            st.title('Matplotlib')
            # 그래프 작성
            fig, ax = plt.subplots()
            ax.hist(iris['sepal_length'], color='Darkgrey')
            st.pyplot(fig)

        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(['탭1', '탭2', '탭3', '탭4'])
        with tab1:
            st.write('탭1')
            # 종류 선택할 때마다
            # 산점도 그래프가 달라지도록 한다.
            # plotly 그래프로 구현
            fig = px.scatter(iris, x='sepal_width',
                             y='sepal_length',
                             color='species',
                             hover_data=['species'])
            st.plotly_chart(fig)

        with tab2:
            st.write('탭2')
            # 캐글 데이터 / 공모전 데이터
            # 해당 데이터 그래프 1개만 그려본다.
            clinical = pd.read_csv('data/supplemental_clinical_data.csv')
            st.write(clinical)

            fig, ax = plt.subplots()
            ax.hist(clinical['updrs_1'], color='purple')
            st.pyplot(fig)

        with tab3:
            st.write('탭3')

        with tab4:
            st.write('탭4')


    elif submenu == '통계분석':
        pass
    else:
        st.waring("WARING──!")


