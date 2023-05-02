# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image

def run_home_app():
    # Config
    st.set_page_config(
        page_title='Cross Chain Monitoring Tool',
        page_icon=':bar_chart:',
        layout='wide'
    )
    # Title
    st.title("AMP®-Parkinson's Disease Progression Prediction")
    st.write(
        """
        Use protein and peptide data measurements from Parkinson's Disease patients to predict progression of the disease.
        """
    )