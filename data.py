# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import utils
from pathlib import Path
# from utils import load_data

@st.cache_data
def load_data():
    # train
    train_comp_dir = Path('data/train')

    target = pd.read_csv(train_comp_dir / 'train_clinical_data.csv')
    sup_target = pd.read_csv(train_comp_dir / 'supplemental_clinical_data.csv')
    train_peptides = pd.read_csv(train_comp_dir / 'train_peptides.csv')
    train_protiens = pd.read_csv(train_comp_dir / 'train_proteins.csv')

    # test
    test_comp_dir = Path('data/test')

    test_peptides = pd.read_csv(test_comp_dir / 'test_peptides.csv')
    test_proteins = pd.read_csv(test_comp_dir / 'test_proteins.csv')
    sample_submission = pd.read_csv(test_comp_dir / 'sample_submission.csv')
    test = pd.read_csv(test_comp_dir / 'test.csv')

    return target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test

def show_data(target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test):
    st.markdown("## target data")
    st.dataframe(target, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## sup_target data")
    st.dataframe(sup_target, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## train_peptides data")
    st.dataframe(train_peptides, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## train_protiens data")
    st.dataframe(train_protiens, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## test_peptides data")
    st.dataframe(test_peptides, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## test_proteins data")
    st.dataframe(test_proteins, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## sample_submission data")
    st.dataframe(sample_submission, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## test data")
    st.dataframe(test, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

def show_chart(target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test):

    combined = pd.concat([target,sup_target]).reset_index(drop=True)

    fig = px.histogram(combined, x="visit_month", color="origin", nbins=30,
                       marginal=None, histnorm="percent",
                       template="plotly_white")

    fig.update_layout(title={
        'text': "Visit Month by Data Source",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title="Visit Month",
        yaxis_title="Percentage",
        font=dict(size=15))

    fig.update_traces(opacity=0.75)

    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- As can be seen in the graph above, we can divide the oil price trend into **<span style='color:#F1C40F'>three phases</span>**. The first and last of these, Jan2013-Jul2014 and Jan2015-Jul2107 respectively, show stabilised trends with ups and downs. However, in the second phase, Jul2014-Jan2015, oil prices decrease considerably. \n"
                "- Now, taking into account the issue of missing values for oil price, we are going to fill them by **<span style='color:#F1C40F'>backward fill technique</span>**. That means filling missing values with next data point (Forward filling means fill missing values with previous data", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

def run_data():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Data</span>",
        unsafe_allow_html=True)
    target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test = load_data()
    submenu = st.sidebar.selectbox("Submenu", ['Show Data', 'Charts'])
    if submenu == 'Show Data':
        show_data(target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test)
    elif submenu == 'Charts':
        show_chart(target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test)
    else:
        pass