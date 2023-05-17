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

    submenu = st.sidebar.selectbox("📋 Stat Menu", ['Basic Statistical Analysis', 'Correlation Analysis', 'Metrics'])

    if submenu == 'Basic Statistical Analysis':
        st.markdown("<h3 style='text-align: center; color: black;'> Two-sample t-test </span>",unsafe_allow_html=True)
        image2 = Image.open('img/sample.png')
        st.image(image2)
        st.markdown("- null hypothesis (H0) : medication On and Off averages are equal.\n"
                    "- alternative hypothesis (H1) : medication On and Off averages are equal.",unsafe_allow_html=True)
        st.markdown("- t-test result : p-value < 0.05.\n"
                    "\n   ☞ H0 rejection & H1 acception.",unsafe_allow_html=True)
        st.markdown("<h4> ✔️ Therefore, the average for medication on and off is different.</h4>",unsafe_allow_html=True)
        st.write('<hr>', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: black;'> Analysis of Medication On/Off - Updrs score </span>",unsafe_allow_html=True)
        image = Image.open('img/ML_1.png')
        st.image(image, caption='Mean of UPDRS')
    elif submenu == 'Correlation Analysis':
        run_stat_box()
        st.write('<hr>', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: black;'> Correlation of Total data </span>",unsafe_allow_html=True)
        image2 = Image.open('img/total.png')
        st.image(image2)
        st.markdown("Ⅰ  -  **visit_month - updrs scores**\n"
                    "- updrs_1, 4 : weak positive correlation ( 0.1, 0.17 ).",
                    unsafe_allow_html=True)
        st.markdown("Ⅱ  -  **Correlation between updrs scores**\n"
                    "- updrs_1 - 2 : Positive correlation ( 0.62 )\n"
                    "- updrs_2 - 3 : Positive correlation ( 0.82 )",
                    unsafe_allow_html=True)
        st.markdown("Ⅲ  -  **NPX - PeptideAbundance**\n"
                    "- Positive correlation ( 0.64 ).",
                    unsafe_allow_html=True)
        st.markdown("Ⅳ  -  **updrs - NPX & PeptideAbundance**\n"
                    "- There are no correlation between updrs - NPX and updrs-PeptideAbundance.",unsafe_allow_html=True)
    elif submenu == 'Metrics':
        run_stat_box_2()







