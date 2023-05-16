# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image

def image_1():
    image_1 = Image.open('img/updrs_1.png')

    st.image(image_1)


def image_2():
    image_2 = Image.open('img/updrs_2.png')

    st.image(image_2)


def image_3():
    image_3 = Image.open('img/updrs_3.png')

    st.image(image_3)


def image_4():
    image_4 = Image.open('img/updrs_4.png')

    st.image(image_4)

def run_stat_box():
    submenu = st.selectbox("⏏️ Correlation of visit_month-updrs score", ['UPDRS_1', 'UPDRS_2','UPDRS_3', 'UPDRS_4'])

    if submenu == 'UPDRS_1':
        image_1()
    elif submenu == 'UPDRS_2':
        image_2()
    elif submenu == 'UPDRS_3':
        image_3()
    elif submenu == 'UPDRS_4':
        image_4()

def image_5():
    image_5 = Image.open('img/metric_1.png')

    st.image(image_5)

    st.markdown(":pencil: **UPDRS_4 != 0:**\n"
    "- The metric MAE, MSE, and R2 are not significantly affected by the value of  of Updrs_4.",
    unsafe_allow_html=True)

def image_6():
    image_6 = Image.open('img/metric_2.png')

    st.image(image_6)

    st.markdown(":pencil: **UPDRS_4 = 0:**\n"
    "- The metric SMAPE are significantly affected by the value of  of Updrs_4.",
    unsafe_allow_html=True)

def run_stat_box_2():
    submenu = st.selectbox("⏏️ 4 Metrics", ['UPDRS_4 != 0', 'UPDRS_4 = 0'])

    if submenu == 'UPDRS_4 != 0':
        image_5()
    elif submenu == 'UPDRS_4 = 0':
        image_6()

def run_status():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Stat</span>",
        unsafe_allow_html=True)

    image = Image.open('img/ml_1.png')
    st.image(image, caption='Mean of UPDRS')

    st.write('<hr>', unsafe_allow_html=True)

    run_stat_box()

    st.write('<hr>', unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: black;'> Correlation of Total data </span>",unsafe_allow_html=True)
    image2 = Image.open('img/total.png')
    st.image(image2)

    st.write('<hr>', unsafe_allow_html=True)

    run_stat_box_2()







