# -*- coding:UTF-8 -*-
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from description import run_description
from data import run_data
from ml_app import run_ml_app
from streamlit_option_menu import option_menu
from eda_app import run_eda

# Confit
st.set_page_config(page_title='Parkinson Disease Progression Prediction', page_icon=':medical_symbol:')
# st.set_page_config(page_title='Parkinson Disease Progression Prediction', page_icon=':medical_symbol:', layout='wide')

def main():
    with st.sidebar:
        selected = option_menu("Main Menu", ['Home', 'Description', 'Data', 'EDA', 'STAT'],
                icons=['house', 'card-checklist', 'card-checklist', 'bar-chart', 'clipboard-data'],
                menu_icon="cast", default_index=0, orientation = 'vertical')

    if selected == 'Home':
        st.markdown("<h1 style='text-align: center; color: darkblue;'>AMP®-Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Disease Progression Prediction</span>",
            unsafe_allow_html=True)

        # Tool
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.image(Image.open('data/excel.png'))
        c2.image(Image.open('data/powerpoint.png'))
        c3.image(Image.open('data/kaggle.png'))
        c4.image(Image.open('data/python.png'))
        c5.image(Image.open('data/pycharm.png'))

        # Content
        st.markdown("<h4 style='font-size: 24px; color: black;'>🔍 Goal of the Competition</h4>", unsafe_allow_html=True)
        st.write(
            """
    The goal of this competition is to predict MDS-UPDR scores, which measure progression in patients with Parkinson's disease. 
    The Movement Disorder Society-Sponsored Revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS) is a comprehensive assessment of both motor and non-motor symptoms associated with Parkinson's. 
    You will develop a model trained on data of protein and peptide levels over time in subjects with Parkinson’s disease versus normal age-matched control subjects.
    
    Your work could help provide important breakthrough information about which molecules change as Parkinson’s disease progresses.
            """
        )

        st.write('<hr>', unsafe_allow_html=True)

        st.markdown("<h5 style='font-size: 24px; color: black;'>🔬 Context</h5>", unsafe_allow_html=True)
        st.write(
            """
    Parkinson’s disease (PD) is a disabling brain disorder that affects movements, cognition, sleep, and other normal functions. 
    Unfortunately, there is no current cure—and the disease worsens over time. It's estimated that by 2037, 1.6 million people in the U.S. will have Parkinson’s disease, 
    at an economic cost approaching $80 billion. Research indicates that protein or peptide abnormalities play a key role in the onset and worsening of this disease. 
    Gaining a better understanding of this—with the help of data science—could provide important clues for the development of new pharmacotherapies to slow the progression or cure Parkinson’s disease.
    
    Current efforts have resulted in complex clinical and neurobiological data on over 10,000 subjects for broad sharing with the research community. 
    A number of important findings have been published using this data, but clear biomarkers or cures are still lacking.
    
    Competition host, the Accelerating Medicines Partnership® Parkinson’s Disease (AMP®PD), is a public-private partnership between government, industry, and nonprofits that is managed through the Foundation of the National Institutes of Health (FNIH). 
    The Partnership created the AMP PD Knowledge Platform, which includes a deep molecular characterization and longitudinal clinical profiling of Parkinson’s disease patients, with the goal of identifying and validating diagnostic, prognostic, and/or disease progression biomarkers for Parkinson’s disease.
    
    Your work could help in the search for a cure for Parkinson’s disease, which would alleviate the substantial suffering and medical care costs of patients with this disease.
            """
        )

        # Link
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info('**Data Analyst: [@Sung](https://muhanyuljung.tistory.com/)**', icon="💡")
        with c2:
            st.info('**GitHub: [@MST](https://github.com/MoonStyIe/Parkinson)**', icon="💻")
        with c3:
            st.info(
                '**Data: [Kaggle](https://www.kaggle.com/competitions/amp-parkinsons-disease-progression-prediction)**',
                icon="🧠")

    elif selected == 'Description':
        run_description()
    elif selected == 'Data':
        run_data()
    elif selected == 'EDA':
        run_eda()
    elif selected == 'STAT':
        pass
    else:
        print('error..')

if __name__ == "__main__":
    main()